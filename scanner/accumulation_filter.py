from config import settings
from models.market_snapshot import MarketSnapshot


class AccumulationFilter:
    def is_valid(self, snapshot: MarketSnapshot) -> bool:
        if snapshot.crash_percent < settings.MIN_CRASH_PERCENT:
            return False
        if snapshot.range_30d_percent > settings.MAX_30D_RANGE_PERCENT:
            return False
        if snapshot.position_in_range > settings.MAX_POSITION_IN_RANGE:
            return False
        return True
