class LeverageFilter:
    @staticmethod
    def accept(snapshot, threshold_min: float = 4.0, threshold_max: float = 10.0) -> bool:
        return threshold_min <= snapshot.max_leverage <= threshold_max
