from config import settings
from models.opportunity import Opportunity


class Ranker:
    def rank(self, snapshots):
        ranked = sorted(snapshots, key=lambda item: item.sleeping_score, reverse=True)
        return [
            Opportunity(
                symbol=item.symbol,
                current_price=item.current_price,
                low_30d=item.low_30d,
                distance_pct=item.distance,
                volume_24h=item.volume_24h,
                funding_rate=item.funding_rate,
                open_interest=item.open_interest,
                score=item.sleeping_score,
                crash_pct=item.crash_percent,
                crash_score=item.crash_score,
                accumulation_score=item.accumulation_score,
                accumulation_days=item.accumulation_days,
                compression_percent=item.compression_percent,
                compression_score=item.compression_score,
                bottom_stability_percent=item.bottom_stability_percent,
                bottom_stability_score=item.bottom_stability_score,
                vol_dryup=item.volume_dryup_percent,
            )
            for item in ranked[:settings.TOP_RESULTS]
        ]
