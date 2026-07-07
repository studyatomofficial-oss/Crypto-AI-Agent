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
        return snapshot
