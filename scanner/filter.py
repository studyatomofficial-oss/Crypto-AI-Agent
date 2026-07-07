from config import MAX_DISTANCE_FROM_LOW, MIN_OPEN_INTEREST, MIN_VOLUME_24H
from models.market_snapshot import MarketSnapshot


class OpportunityFilter:
    def is_qualified(self, snapshot: MarketSnapshot) -> bool:
        return (
            snapshot.distance <= MAX_DISTANCE_FROM_LOW
            and snapshot.volume_24h >= MIN_VOLUME_24H
            and snapshot.open_interest >= MIN_OPEN_INTEREST
        )
