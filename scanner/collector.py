from services.market_service import MarketService
from scanner.cache import MarketCache
from models.market_snapshot import MarketSnapshot
from database.oi_history import OIHistoryRepository


class MarketCollector:
    def __init__(
        self,
        market: MarketService,
        cache: MarketCache,
        oi_history: OIHistoryRepository,
    ) -> None:
        self.market = market
        self.cache = cache
        self.oi_history = oi_history

    def collect(self, symbol: str) -> MarketSnapshot:
        ticker = self.cache.get(symbol)
        if ticker is None:
            raise ValueError(f"{symbol} not found in MarketCache")

        current_price = float(ticker["lastPrice"])
        candles = self.market.get_candles(symbol)
        low_30d = min((candle.low for candle in candles), default=0.0)
        current_open_interest = self.market.get_open_interest(symbol)
        oi_change_30d = self.oi_history.compute_30d_change(
            symbol,
            current_open_interest,
        )
        self.oi_history.upsert_daily(symbol, current_open_interest)
        snapshot = MarketSnapshot(
            symbol=symbol,
            current_price=current_price,
            low_30d=low_30d,
            volume_24h=float(ticker["volume24h"]),
            turnover_24h=float(ticker["turnover24h"]),
            funding_rate=float(ticker["fundingRate"]),
            open_interest=current_open_interest,
            oi_change_30d=oi_change_30d,
        )
        snapshot.candles = candles
        return snapshot
