from models.market_snapshot import MarketSnapshot


class SleepingScorer:
    @staticmethod
    def _crash_score(crash: float) -> float:
        # Continuous: (crash - 40) * 2, clamped 0-100
        return min(100.0, max(0.0, (crash - 40) * 2))

    @staticmethod
    def _accumulation_score(days: int) -> float:
        # Continuous: days / 0.45, clamped 0-100
        # At 45 days = 100, linear from 0
        return min(100.0, max(0.0, days * 100.0 / 45.0))

    @staticmethod
    def _compression_score(compression: float) -> float:
        # Continuous: lower is better
        # Max 100 at <=5%, min 0 at >=60%
        # Linear: (60 - compression) / 60 * 100
        return min(100.0, max(0.0, (60.0 - compression) * 100.0 / 60.0))

    @staticmethod
    def _bottom_stability_score(value: float) -> float:
        # Continuous: lower is better
        # Max 100 at <=2%, min 0 at >=20%
        # Linear: (20 - value) / 18 * 100
        return min(100.0, max(0.0, (20.0 - value) * 100.0 / 18.0))

    @staticmethod
    def _recovery_score(value: float) -> float:
        # Continuous: lower is better
        # Max 100 at <=5%, min 0 at >=50%
        # Linear: (50 - value) / 45 * 100
        return min(100.0, max(0.0, (50.0 - value) * 100.0 / 45.0))

    def score(self, snapshot: MarketSnapshot) -> None:
        snapshot.crash_score = self._crash_score(snapshot.crash_percent)
        snapshot.accumulation_score = self._accumulation_score(
            snapshot.accumulation_days
        )
        snapshot.compression_score = self._compression_score(
            snapshot.compression_percent
        )
        snapshot.bottom_stability_score = self._bottom_stability_score(
            snapshot.bottom_stability_percent
        )
        snapshot.recovery_score = self._recovery_score(
            snapshot.recovery_percent
        )
        # Weighted composition: max score = 100
        snapshot.sleeping_score = (
            snapshot.crash_score * 0.40
            + snapshot.accumulation_score * 0.25
            + snapshot.compression_score * 0.20
            + snapshot.bottom_stability_score * 0.10
            + snapshot.recovery_score * 0.05
        )
