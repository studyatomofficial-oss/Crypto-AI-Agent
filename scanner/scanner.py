from scanner.universe import UniverseBuilder
from scanner.collector import MarketCollector
from scanner.analyzer import SnapshotAnalyzer
from scanner.ranker import Ranker
from scanner.reporter import Reporter
from scanner.cache import MarketCache


class Scanner:
    def __init__(self) -> None:
        self.market = UniverseBuilder().market
        self.cache = MarketCache()
        self.universe_builder = UniverseBuilder()
        self.collector = MarketCollector(self.market, self.cache)
        self.analyzer = SnapshotAnalyzer()
        self.ranker = Ranker()
        self.reporter = Reporter()

    def run(self) -> None:
        tickers = self.universe_builder.market.get_all_tickers()
        self.cache.load(tickers)
        print()
        print(f"Cached {self.cache.size} tickers.")
        print()

        btc = self.cache.get("BTCUSDT")
        print(btc)

        symbols = self.universe_builder.build()
        snapshots = []
        for coin in symbols:
            snapshot = self.collector.collect(coin["symbol"])
            snapshot = self.analyzer.analyze(snapshot)
            snapshots.append(snapshot)

        ranked = self.ranker.rank(snapshots)
        self.reporter.report(ranked[:10])
