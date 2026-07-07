from models.candle import Candle
from models.market_snapshot import MarketSnapshot
from indicators.ema import EMA


class MarketAnalyzer:
    def __init__(self) -> None:
        self.indicators = [EMA(20), EMA(50)]

    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> MarketSnapshot:
        if snapshot.low_30d == 0.0:
            snapshot.score = 0.0
            return snapshot
        snapshot.distance = ((snapshot.current_price - snapshot.low_30d) / snapshot.low_30d) * 100
        for indicator in self.indicators:
            indicator.calculate(snapshot, candles)
        snapshot.score = self.score(snapshot)
        return snapshot

    def score(self, snapshot: MarketSnapshot) -> float:
        from config import settings
        distance_score = max(0.0, 50.0 - snapshot.distance * 10.0)
        volume_score = min(25.0, snapshot.volume_24h / settings.MIN_VOLUME_24H * 12.5)
        oi_score = min(15.0, snapshot.open_interest / settings.MIN_OPEN_INTEREST * 7.5)
        funding_score = 10.0 if snapshot.funding_rate < 0 else max(0.0, 10.0 - abs(snapshot.funding_rate) * 100_000.0)
        return round((distance_score) + (volume_score) + (oi_score) + (funding_score), 2)
