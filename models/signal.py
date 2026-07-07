from dataclasses import dataclass


@dataclass
class Signal:
    symbol: str
    current_price: float
    low_price: float
    distance: float
