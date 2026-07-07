from models.opportunity import Opportunity


class Ranker:
    def rank(self, snapshots):
        ranked = sorted(snapshots, key=lambda item: item.score, reverse=True)
        return [
            Opportunity(
                symbol=item.symbol,
                current_price=item.current_price,
                low_30d=item.low_30d,
                distance_pct=item.distance,
                volume_24h=item.volume_24h,
                funding_rate=item.funding_rate,
                open_interest=item.open_interest,
                score=item.score,
            )
            for item in ranked
        ]
