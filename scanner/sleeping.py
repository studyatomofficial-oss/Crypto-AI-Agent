from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class SleepingAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return

        # Days near bottom
        threshold = snapshot.low_30d * 1.05
        snapshot.days_near_bottom = sum(
            1 for candle in candles if candle.close <= threshold
        )

        # Average daily range
        ranges = [
            ((candle.high - candle.low) / candle.low) * 100
            for candle in candles
            if candle.low > 0
        ]
        snapshot.average_daily_range = sum(ranges) / len(ranges) if ranges else 0.0

        # Volume dry-up
        avg_volume = sum(c.volume for c in candles) / len(candles)
        snapshot.volume_dryup_percent = (
            (snapshot.volume_24h / avg_volume) * 100 if avg_volume > 0 else 0.0
        )

        # Sleeping score
        score = 0.0
        score += snapshot.crash_percent * 0.40
        score += snapshot.days_near_bottom
        score += max(0.0, 25.0 - snapshot.average_daily_range)
        score += max(0.0, 100.0 - snapshot.volume_dryup_percent)
        snapshot.sleeping_score = round(score, 2)
