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

    def score(self, snapshot: MarketSnapshot) -> None:
        snapshot.crash_score = self._crash_score(snapshot.crash_percent)
        snapshot.sleeping_score = snapshot.crash_score
