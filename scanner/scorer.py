from models.market_snapshot import MarketSnapshot


class SleepingScorer:
    @staticmethod
    def _crash_score(crash: float) -> float:
        if crash >= 90:
            return 100
        if crash >= 80:
            return 90
        if crash >= 70:
            return 80
        if crash >= 60:
            return 60
        if crash >= 50:
            return 40
        if crash >= 40:
            return 20
        return 0

    @staticmethod
    def _accumulation_score(days: int) -> float:
        if days >= 45:
            return 100
        if days >= 35:
            return 90
        if days >= 30:
            return 80
        if days >= 25:
            return 70
        if days >= 20:
            return 60
        if days >= 15:
            return 40
        if days >= 10:
            return 20
        return 0

    @staticmethod
    def _compression_score(compression: float) -> float:
        if compression <= 5:
            return 100
        if compression <= 10:
            return 90
        if compression <= 15:
            return 80
        if compression <= 20:
            return 70
        if compression <= 30:
            return 60
        if compression <= 40:
            return 40
        if compression <= 60:
            return 20
        return 0

    @staticmethod
    def _bottom_stability_score(value: float) -> float:
        if value <= 2:
            return 100
        if value <= 4:
            return 90
        if value <= 6:
            return 80
        if value <= 8:
            return 70
        if value <= 10:
            return 60
        if value <= 15:
            return 40
        if value <= 20:
            return 20
        return 0

    @staticmethod
    def _recovery_score(value: float) -> float:
        if value <= 5:
            return 100
        if value <= 10:
            return 90
        if value <= 15:
            return 80
        if value <= 20:
            return 70
        if value <= 30:
            return 50
        if value <= 40:
            return 30
        return 0

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
        snapshot.sleeping_score = (
            snapshot.crash_score
            + snapshot.accumulation_score
            + snapshot.compression_score
            + snapshot.bottom_stability_score
            + snapshot.recovery_score
        )
