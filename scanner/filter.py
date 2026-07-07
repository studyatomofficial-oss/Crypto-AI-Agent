from config import settings
from models.market_snapshot import MarketSnapshot


class OpportunityFilter:
    def is_qualified(self, snapshot: MarketSnapshot) -> bool:
        return (
            snapshot.distance <= settings.MAX_DISTANCE_FROM_LOW
            and snapshot.volume_24h >= settings.MIN_VOLUME_24H
            and snapshot.open_interest >= settings.MIN_OPEN_INTEREST
        )
