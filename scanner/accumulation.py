from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class AccumulationAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return
        high = max(c.high for c in candles)
        low = min(c.low for c in candles)
        midpoint = (high + low) / 2 if high > 0 and low > 0 else 0.0
        snapshot.high_30d = high
        snapshot.compression_percent = (
            ((high - low) / midpoint) * 100 if midpoint > 0 else 0.0
        )
        snapshot.position_in_range = (
            ((snapshot.current_price - low) / (high - low)) * 100
            if high != low
            else 0.0
        )
