from dataclasses import dataclass


@dataclass(slots=True)
class MarketSnapshot:
    symbol: str
    current_price: float
    low_30d: float
    distance: float = 0.0
    volume_24h: float = 0.0
    funding_rate: float = 0.0
    open_interest: float = 0.0
    max_leverage: float = 0.0
    score: float = 0.0
