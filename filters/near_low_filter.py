class NearLowFilter:
    @staticmethod
    def accept(snapshot, threshold: float = 5.0) -> bool:
        return snapshot.distance <= threshold
