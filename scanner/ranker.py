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
                range_30d=item.range_30d_percent,
                position=item.position_in_range,
                days_near_bottom=item.days_near_bottom,
                adr=item.average_daily_range,
                vol_dryup=item.volume_dryup_percent,
            )
            for item in ranked[:settings.TOP_RESULTS]
        ]
