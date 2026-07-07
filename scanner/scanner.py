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
from config import settings


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

    def run(self) -> None:
        tickers = self.universe_builder.market.get_all_tickers()
        self.cache.load(tickers)
        print(f"Cached {self.cache.size} tickers.")

        symbols = self.universe_builder.build()
        snapshots = []
        for coin in symbols:
            try:
                snapshot = self.collector.collect(coin["symbol"])
                candles_90 = self.market.get_candles(coin["symbol"], settings.CRASH_LOOKBACK_DAYS)
                self.crash.analyze(snapshot, candles_90)
                self.recovery.analyze(snapshot)
                self.sleeping.calculate_accumulation_days(snapshot, candles_90)
                candles_30 = self.market.get_candles(coin["symbol"], settings.ACCUMULATION_LOOKBACK_DAYS)
                self.accumulation.analyze(snapshot, candles_30)
                self.sleeping.analyze(snapshot, candles_30)
                self.scorer.score(snapshot)
                snapshots.append(snapshot)
            except Exception as e:
                print(f"{coin['symbol']} -> {e}")

        ranked = self.ranker.rank(snapshots)
        ConsoleReport().show(ranked)
        self.csv_report.save(ranked)
