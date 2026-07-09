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

    @staticmethod
    def _percent_vs_average(current_value: float, average_value: float | None) -> float:
        if average_value is None or average_value <= 0:
            return 0.0
        return ((current_value - average_value) / average_value) * 100.0

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
        oi_avg_7d = self.oi_history.get_average_open_interest(symbol, days_back=7)
        oi_avg_30d = self.oi_history.get_average_open_interest(symbol, days_back=30)
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
            oi_avg_7d=oi_avg_7d or 0.0,
            oi_avg_30d=oi_avg_30d or 0.0,
            oi_vs_7d_avg=self._percent_vs_average(current_open_interest, oi_avg_7d),
            oi_vs_30d_avg=self._percent_vs_average(current_open_interest, oi_avg_30d),
        )
        snapshot.candles = candles
        return snapshot
