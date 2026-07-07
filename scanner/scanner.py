from scanner.universe import UniverseBuilder
from scanner.collector import MarketCollector
from scanner.analyzer import SnapshotAnalyzer
from scanner.crash import CrashAnalyzer
from scanner.ranker import Ranker
from scanner.cache import MarketCache
from reports.console_report import ConsoleReport
from config import settings


class Scanner:
    def __init__(self) -> None:
        self.market = UniverseBuilder().market
        self.cache = MarketCache()
        self.universe_builder = UniverseBuilder()
        self.collector = MarketCollector(self.market, self.cache)
        self.analyzer = SnapshotAnalyzer()
        self.crash = CrashAnalyzer()
        self.ranker = Ranker()

    def run(self) -> None:
        tickers = self.universe_builder.market.get_all_tickers()
        self.cache.load(tickers)
        print(f"Cached {self.cache.size} tickers.")

        symbols = self.universe_builder.build()
        snapshots = []
        for coin in symbols:
            try:
                snapshot = self.collector.collect(coin["symbol"])
                candles_90 = self.market.get_candles(coin["symbol"], settings.LOOKBACK_90D)
                self.crash.analyze(snapshot, candles_90)
                print("=" * 60)
                print(snapshot.symbol)
                print(f"Current  : {snapshot.current_price}")
                print(f"90D High : {snapshot.high_90d}")
                print(f"Crash    : {snapshot.crash_percent:.2f}%")
                snapshot = self.analyzer.analyze(snapshot)
                if not snapshot.is_qualified:
                    continue
                snapshots.append(snapshot)
            except Exception as e:
                print(f"{coin['symbol']} -> {e}")

        ranked = self.ranker.rank(snapshots)
        ConsoleReport().show(ranked)
