class FundingFilter:
    @staticmethod
    def accept(snapshot, threshold: float = 0.001) -> bool:
        return abs(snapshot.funding_rate) <= threshold
