from models.market_snapshot import MarketSnapshot


class MarketAnalyzer:
    @staticmethod
    def calculate_distance(snapshot: MarketSnapshot) -> MarketSnapshot:
        snapshot.distance = ((snapshot.current_price - snapshot.low_30d) / snapshot.low_30d) * 100
        return snapshot
