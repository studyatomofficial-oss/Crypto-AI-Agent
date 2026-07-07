from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class AccumulationAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return
        high = max(c.high for c in candles)
        low = min(c.low for c in candles)
        snapshot.high_30d = high
        snapshot.range_30d_percent = ((high - low) / low) * 100
        snapshot.position_in_range = (
            ((snapshot.current_price - low) / (high - low)) * 100
            if high != low
            else 0.0
        )
