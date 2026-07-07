from services.market_service import MarketService


class UniverseBuilder:
    def __init__(self) -> None:
        self.market = MarketService()

    def build(self) -> list[dict]:
        return self.market.get_tradeable_symbols()
