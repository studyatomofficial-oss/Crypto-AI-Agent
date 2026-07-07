from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class CrashAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return
        high_90d = max(candle.high for candle in candles)
        snapshot.high_90d = high_90d
        if high_90d > 0:
            snapshot.crash_percent = ((high_90d - snapshot.current_price) / high_90d) * 100
