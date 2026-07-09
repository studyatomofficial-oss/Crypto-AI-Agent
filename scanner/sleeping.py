from config import settings
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

        # Volume dry-up as reduction percentage vs average daily volume.
        avg_volume = sum(c.volume for c in candles) / len(candles)
        if avg_volume > 0:
            snapshot.volume_dryup_percent = max(
                0.0,
                (1 - (snapshot.volume_24h / avg_volume)) * 100,
            )
        else:
            snapshot.volume_dryup_percent = 0.0
        snapshot.volume_dryup = snapshot.volume_dryup_percent

        # Stable base proxy: average daily range over the lookback period.
        daily_ranges = [
            ((candle.high - candle.low) / candle.close) * 100
            for candle in candles
            if candle.close > 0
        ]
        snapshot.avg_daily_range = (
            sum(daily_ranges) / len(daily_ranges)
            if daily_ranges
            else 0.0
        )

    def calculate_accumulation_days(
        self,
        snapshot: MarketSnapshot,
        candles: list[Candle],
    ) -> None:
        if not candles:
            return
        threshold = snapshot.low_30d * (
            1 + settings.BOTTOM_ZONE_PERCENT / 100
        )
        count = 0
        for candle in candles:
            if candle.close <= threshold:
                count += 1
            else:
                count = 0
        snapshot.accumulation_days = count
