from services.market_service import MarketService
from models.market_snapshot import MarketSnapshot


class MarketCollector:
    def __init__(self) -> None:
        self.market = MarketService()

    def collect(self, symbol: str) -> MarketSnapshot:
        data = self.market.get_market_snapshot(symbol)
        return MarketSnapshot(
            symbol=data["symbol"],
            current_price=data["current_price"],
            low_30d=data["low_30d"],
            distance=data["distance"],
        )
