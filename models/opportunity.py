from dataclasses import dataclass


@dataclass(slots=True)
class Opportunity:
    symbol: str
    current_price: float
    low_30d: float
    distance_pct: float
    volume_24h: float
    funding_rate: float
    open_interest: float
    funding_score: float
    psychology_score: float
    final_score: float
    score: float
    crash_pct: float = 0.0
    crash_score: float = 0.0
    accumulation_score: float = 0.0
    accumulation_days: int = 0
    compression_percent: float = 0.0
    compression_score: float = 0.0
    bottom_stability_percent: float = 0.0
    bottom_stability_score: float = 0.0
    recovery_percent: float = 0.0
    recovery_score: float = 0.0
    vol_dryup: float = 0.0
    reason: str = ""
