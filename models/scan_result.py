from dataclasses import dataclass
from typing import List
from models.market_snapshot import MarketSnapshot


@dataclass(slots=True)
class ScanResult:
    snapshots: List[MarketSnapshot]
