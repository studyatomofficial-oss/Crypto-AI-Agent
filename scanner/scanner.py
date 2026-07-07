import time
from scanner.universe import UniverseBuilder
from scanner.recovery import RecoveryAnalyzer
from scanner.collector import MarketCollector
from scanner.analyzer import SnapshotAnalyzer
from scanner.crash import CrashAnalyzer
from scanner.accumulation import AccumulationAnalyzer
from scanner.sleeping import SleepingAnalyzer
from scanner.scorer import SleepingScorer
from scanner.ranker import Ranker
from scanner.cache import MarketCache
from reports.console_report import ConsoleReport
from reports.csv_report import CsvReport
from reports.change_detector import ChangeDetector
from utils.progress import ProgressBar
from utils.logger import get_logger
from config import settings
import strategy


class Scanner:
    def __init__(self) -> None:
        self.market = UniverseBuilder().market
        self.cache = MarketCache()
        self.universe_builder = UniverseBuilder()
        self.collector = MarketCollector(self.market, self.cache)
        self.analyzer = SnapshotAnalyzer()
        self.crash = CrashAnalyzer()
        self.recovery = RecoveryAnalyzer()
        self.accumulation = AccumulationAnalyzer()
        self.sleeping = SleepingAnalyzer()
        self.scorer = SleepingScorer()
        self.ranker = Ranker()
        self.csv_report = CsvReport()
        self.change_detector = ChangeDetector()
        self.logger = get_logger(__name__)

    def run(self) -> None:
        print()
        print("=" * 60)
        print(f"{strategy.STRATEGY_NAME}")
        print(f"Version     : {strategy.VERSION}")
        print(f"Strategy    : {strategy.STRATEGY_DESCRIPTION}")
        print(f"Exchange    : {strategy.EXCHANGE}")
        print(f"Universe    : {strategy.UNIVERSE}")
        print("=" * 60)
        print()

        start_time = time.perf_counter()
        tickers = self.universe_builder.market.get_all_tickers()
        self.cache.load(tickers)
        print(f"Cached {self.cache.size} tickers.")

        symbols = self.universe_builder.build()

        print()
        print(">> Starting Sleeping Giants Scan...")
        print(f"Eligible Contracts : {len(symbols)}")
        print()

        progress = ProgressBar(len(symbols))
        snapshots = []
        failed_symbols = []
        for index, coin in enumerate(symbols, start=1):
            try:
                snapshot = self.collector.collect(coin["symbol"])
                
                if snapshot.current_price <= 0:
                    raise ValueError("Invalid current price")
                
                candles_90 = self.market.get_candles(coin["symbol"], settings.CRASH_LOOKBACK_DAYS)
                self.crash.analyze(snapshot, candles_90)
                
                if snapshot.high_90d <= 0:
                    raise ValueError("Invalid 90d high")
                
                self.recovery.analyze(snapshot)
                self.sleeping.calculate_accumulation_days(snapshot, candles_90)
                candles_30 = self.market.get_candles(coin["symbol"], settings.ACCUMULATION_LOOKBACK_DAYS)
                self.accumulation.analyze(snapshot, candles_30)
                self.sleeping.analyze(snapshot, candles_30)
                
                if snapshot.low_30d <= 0:
                    raise ValueError("Invalid 30d low")
                
                self.scorer.score(snapshot)
                snapshots.append(snapshot)
            except Exception as e:
                error_msg = str(e)
                failed_symbols.append((coin["symbol"], error_msg))
                self.logger.info(f"{coin['symbol']}: {error_msg}")
            finally:
                progress.update(index)

        progress.finish()

        end_time = time.perf_counter()
        scan_duration = end_time - start_time

        print()
        print(">> Scan Complete!")
        print()

        ranked = self.ranker.rank(snapshots)
        ConsoleReport().show(ranked)
        csv_files = self.csv_report.save(ranked)

        print()
        print("=" * 55)
        print("SCAN SUMMARY")
        print("=" * 55)
        print()
        print(f"Universe               : {len(symbols)}")
        print(f"Top Results            : {len(ranked)}")
        print(f"Strategy               : 1.0.0")
        print()

        print(f"Scan ID                : {csv_files['scan_id']}")
        print(f"Scan Duration          : {scan_duration:.2f} sec")
        print()

        print(f"Latest CSV             : output/{csv_files['latest']}")
        print(f"History CSV            : output/history/{csv_files['history']}")
        print("=" * 55)

        if failed_symbols:
            print()
            print("=" * 60)
            print("FAILED SYMBOLS")
            print("=" * 60)
            for symbol, error in failed_symbols:
                print(f"{symbol:<20} {error}")
            print("=" * 60)

        changes = self.change_detector.compare()
        if changes:
            self.change_detector.report(changes)
