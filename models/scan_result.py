from dataclasses import dataclass
from typing import List
from models.market_snapshot import MarketSnapshot
from models.opportunity import Opportunity


@dataclass(slots=True)
class ScanResult:
    snapshots: List[MarketSnapshot]
    opportunities: List[Opportunity]
