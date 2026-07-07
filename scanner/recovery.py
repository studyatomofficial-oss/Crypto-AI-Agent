from models.market_snapshot import MarketSnapshot


class RecoveryAnalyzer:
    def analyze(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        move = snapshot.high_90d - snapshot.low_30d
        if move <= 0:
            snapshot.recovery_percent = 100
            return
        snapshot.recovery_percent = (
            (snapshot.current_price - snapshot.low_30d)
            / move
        ) * 100
