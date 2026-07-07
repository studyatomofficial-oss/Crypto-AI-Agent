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
    score: float
    crash_pct: float = 0.0
    crash_score: float = 0.0
    accumulation_score: float = 0.0
    compression_percent: float = 0.0
    compression_score: float = 0.0
    position: float = 0.0
    days_near_bottom: int = 0
    vol_dryup: float = 0.0
