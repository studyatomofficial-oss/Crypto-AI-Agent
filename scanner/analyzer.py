from analyzers.market_analyzer import MarketAnalyzer


class SnapshotAnalyzer:
    def __init__(self) -> None:
        self.analyzer = MarketAnalyzer()

    def analyze(self, snapshot):
        return self.analyzer.analyze(snapshot, snapshot.candles)
