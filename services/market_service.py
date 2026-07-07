from api.bybit import BybitClient
from config import settings
from models.candle import Candle


class MarketService:
    def __init__(self) -> None:
        self.bybit = BybitClient()

    def get_tradeable_symbols(self) -> list[dict]:
        symbols = []
        cursor = None
        while True:
            response = self.bybit.get_all_instruments(cursor=cursor)
            result = response["result"]
            for coin in result["list"]:
                if coin["status"] != "Trading":
                    continue
                if coin["contractType"] != "LinearPerpetual":
                    continue
                leverage = float(coin["leverageFilter"]["maxLeverage"])
                if settings.MIN_LEVERAGE <= leverage <= settings.MAX_LEVERAGE:
                    symbols.append(coin)
            cursor = result.get("nextPageCursor")
            if not cursor:
                break
        return symbols

    def get_last_30_days(self, symbol: str) -> list[Candle]:
        response = self.bybit.get_kline(symbol, limit=settings.LOOKBACK_DAYS)
        candle_items = response.get("result", {}).get("list", [])
        candles = []
        for item in candle_items:
            if not isinstance(item, list):
                continue
            candles.append(Candle.from_api(item))
        return candles

    def get_open_interest(self, symbol: str) -> float:
        response = self.bybit.get_open_interest(symbol)
        data = response.get("result", {}).get("list", [])
        if not data:
            return 0.0
        return float(data[0]["openInterest"])

    def get_30_day_low(self, symbol: str) -> float:
        candles = self.get_last_30_days(symbol)
        return min(candle.low for candle in candles)

    def get_all_tickers(self) -> list[dict]:
        response = self.bybit.get_all_tickers()
        return response["result"]["list"]

    def get_current_price(self, symbol: str) -> float:
        ticker = self.bybit.get_ticker(symbol)
        return float(ticker["result"]["list"][0]["lastPrice"])

    def get_market_snapshot(self, symbol: str) -> dict:
        current_price = self.get_current_price(symbol)
        low_price = self.get_30_day_low(symbol)
        return {
            "symbol": symbol,
            "current_price": current_price,
            "low_30d": low_price,
            "distance": ((current_price - low_price) / low_price) * 100 if low_price else 0.0,
        }
