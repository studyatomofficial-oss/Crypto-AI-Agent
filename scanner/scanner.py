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
        print("=" * 60)
        print(f"{'Rank':<4} {'Symbol':<10} {'Distance':<10} {'Volume':<12} {'Funding':<10} {'Score':<8}")
        print("-" * 60)
        for index, opportunity in enumerate(ranked, start=1):
            print(
                f"{index:<4} {opportunity.symbol:<10} {opportunity.distance_pct:>8.2f}% {opportunity.volume_24h/1_000_000:>8.2f}M {opportunity.funding_rate:>10.5f} {opportunity.score:>8.1f}"
            )
