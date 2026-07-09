from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class AccumulationAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return
        high = max(c.high for c in candles)
        low = min(c.low for c in candles)
        recent_window = candles[-10:] if len(candles) >= 10 else candles
        closes = [c.close for c in recent_window if c.close > 0]
        average_close = (sum(closes) / len(closes)) if closes else 0.0
        close_range = (max(closes) - min(closes)) if closes else 0.0
        snapshot.high_30d = high
        snapshot.compression_percent = (
            (close_range / average_close) * 100 if average_close > 0 else 0.0
        )
        snapshot.position_in_range = (
            ((snapshot.current_price - low) / (high - low)) * 100
            if high != low
            else 0.0
        )
