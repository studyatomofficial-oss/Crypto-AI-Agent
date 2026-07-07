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
        if days >= 30:
            return 100
        if days >= 27:
            return 90
        if days >= 24:
            return 80
        if days >= 21:
            return 70
        if days >= 18:
            return 60
        if days >= 15:
            return 50
        if days >= 12:
            return 40
        if days >= 9:
            return 30
        if days >= 6:
            return 20
        if days >= 3:
            return 10
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

    def score(self, snapshot: MarketSnapshot) -> None:
        snapshot.crash_score = self._crash_score(snapshot.crash_percent)
        snapshot.accumulation_score = self._accumulation_score(
            snapshot.days_near_bottom
        )
        snapshot.compression_score = self._compression_score(
            snapshot.compression_percent
        )
        snapshot.sleeping_score = (
            snapshot.crash_score
            + snapshot.accumulation_score
            + snapshot.compression_score
        )
