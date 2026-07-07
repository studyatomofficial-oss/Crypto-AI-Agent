from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class SleepingAnalyzer:
    def analyze(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        if not candles:
            return

        # Bottom stability - average distance from 30-day low
        distances = []
        for candle in candles:
            distance = (
                (candle.close - snapshot.low_30d)
                / snapshot.low_30d
            ) * 100
            distances.append(distance)
        snapshot.bottom_stability_percent = (
            sum(distances)
            / len(distances)
        )

        # Days near bottom
        threshold = snapshot.low_30d * 1.05
        snapshot.days_near_bottom = sum(
            1 for candle in candles if candle.close <= threshold
        )

        # Volume dry-up
        avg_volume = sum(c.volume for c in candles) / len(candles)
        snapshot.volume_dryup_percent = (
            (snapshot.volume_24h / avg_volume) * 100 if avg_volume > 0 else 0.0
        )
