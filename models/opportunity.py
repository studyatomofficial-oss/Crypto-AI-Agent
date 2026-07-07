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
    range_30d: float = 0.0
    position: float = 0.0
    days_near_bottom: int = 0
    adr: float = 0.0
    vol_dryup: float = 0.0
