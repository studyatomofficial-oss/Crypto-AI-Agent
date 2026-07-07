from dataclasses import dataclass


@dataclass
class Signal:
    symbol: str
    score: float
    created_at: str
