from models.candle import Candle
from models.market_snapshot import MarketSnapshot
from indicators.ema import EMA


class MarketAnalyzer:
    def __init__(self) -> None:
        self.indicators = [EMA(20), EMA(50)]

    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> MarketSnapshot:
        snapshot.distance = ((snapshot.current_price - snapshot.low_30d) / snapshot.low_30d) * 100
        for indicator in self.indicators:
            indicator.calculate(snapshot, candles)
        snapshot.score = self.score(snapshot)
        return snapshot

    def score(self, snapshot: MarketSnapshot) -> float:
        distance_score = max(0.0, 100.0 - snapshot.distance * 10.0)
        volume_score = min(100.0, snapshot.volume_24h / 50_000.0)
        oi_score = min(100.0, snapshot.open_interest / 10_000.0)
        funding_score = max(0.0, 100.0 - abs(snapshot.funding_rate) * 100_000.0)
        return (distance_score * 0.50) + (volume_score * 0.25) + (oi_score * 0.15) + (funding_score * 0.10)
