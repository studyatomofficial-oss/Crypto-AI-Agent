from config import settings
from models.opportunity import Opportunity


class Ranker:
    @staticmethod
    def _generate_reason(snapshot) -> str:
        """Generate human-readable reason for ranking."""
        parts = [
            f"{snapshot.crash_percent:.0f}% crash",
            f"{snapshot.accumulation_days} bottom days",
            f"{snapshot.compression_percent:.0f}% range",
            f"{snapshot.recovery_percent:.1f}% recovery"
        ]
        return " • ".join(parts)

    def rank(self, snapshots):
        ranked = sorted(snapshots, key=lambda item: item.final_score, reverse=True)
        return [
            Opportunity(
                symbol=item.symbol,
                current_price=item.current_price,
                low_30d=item.low_30d,
                distance_pct=item.distance,
                volume_24h=item.volume_24h,
                funding_rate=item.funding_rate,
                open_interest=item.open_interest,
                oi_change_30d=item.oi_change_30d,
                oi_score=item.oi_score,
                funding_score=item.funding_score,
                crowd_score=item.crowd_score,
                psychology_score=item.psychology_score,
                final_score=item.final_score,
                score=item.sleeping_score,
                crash_pct=item.crash_percent,
                crash_score=item.crash_score,
                accumulation_score=item.accumulation_score,
                accumulation_days=item.accumulation_days,
                compression_percent=item.compression_percent,
                compression_score=item.compression_score,
                bottom_stability_percent=item.bottom_stability_percent,
                bottom_stability_score=item.bottom_stability_score,
                recovery_percent=item.recovery_percent,
                recovery_score=item.recovery_score,
                vol_dryup=item.volume_dryup_percent,
                reason=self._generate_reason(item),
            )
            for item in ranked[:settings.TOP_RESULTS]
        ]
