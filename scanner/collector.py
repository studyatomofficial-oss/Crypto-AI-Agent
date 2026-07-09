from services.market_service import MarketService
from scanner.cache import MarketCache
from models.market_snapshot import MarketSnapshot


class MarketCollector:
    def __init__(self, market: MarketService, cache: MarketCache) -> None:
        self.market = market
        self.cache = cache

    def collect(self, symbol: str) -> MarketSnapshot:
        ticker = self.cache.get(symbol)
        if ticker is None:
            raise ValueError(f"{symbol} not found in MarketCache")

        current_price = float(ticker["lastPrice"])
        candles = self.market.get_candles(symbol)
        low_30d = min((candle.low for candle in candles), default=0.0)
        snapshot = MarketSnapshot(
            symbol=symbol,
            current_price=current_price,
            low_30d=low_30d,
            volume_24h=float(ticker["volume24h"]),
            turnover_24h=float(ticker["turnover24h"]),
            funding_rate=float(ticker["fundingRate"]),
            open_interest=self.market.get_open_interest(symbol),
            # Placeholder until historical OI collection is added.
            oi_change_30d=0.0,
        )
        snapshot.candles = candles
        return snapshot
