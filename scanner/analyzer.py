from analyzers.market_analyzer import MarketAnalyzer
from scanner.filter import OpportunityFilter


class SnapshotAnalyzer:
    def __init__(self) -> None:
        self.analyzer = MarketAnalyzer()
        self.filter = OpportunityFilter()

    def analyze(self, snapshot):
        snapshot = self.analyzer.analyze(snapshot, snapshot.candles)
        snapshot.is_qualified = self.filter.is_qualified(snapshot)
        return snapshot
