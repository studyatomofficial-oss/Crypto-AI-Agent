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
