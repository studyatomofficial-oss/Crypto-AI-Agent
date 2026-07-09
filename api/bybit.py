from api.client import HttpClient
from config import settings


class BybitClient:
    BASE_URL = settings.BYBIT_BASE_URL

    def __init__(self, api_key: str = "", api_secret: str = "") -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = HttpClient(self.BASE_URL)

    def get_server_time(self):
        return self.client.get("/v5/market/time")

    def get_ticker(self, symbol: str):
        return self.client.get(
            "/v5/market/tickers",
            {
                "category": "linear",
                "symbol": symbol,
            },
        )

    def get_all_tickers(self):
        return self.client.get(
            "/v5/market/tickers",
            {
                "category": "linear",
            },
        )

    def get_all_instruments(self, limit: int = 1000, cursor: str | None = None):
        params = {
            "category": "linear",
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        return self.client.get(
            "/v5/market/instruments-info",
            params,
        )

    def get_kline(self, symbol: str, limit: int):
        return self.client.get(
            "/v5/market/kline",
            {
                "category": "linear",
                "symbol": symbol,
                "interval": "D",
                "limit": limit,
            },
        )

    def get_open_interest(self, symbol: str):
        return self.client.get(
            "/v5/market/open-interest",
            {
                "category": "linear",
                "symbol": symbol,
                "intervalTime": "5min",
            },
        )

    def get_open_interest_history(
        self,
        symbol: str,
        interval_time: str = "1d",
        limit: int = 30,
    ):
        return self.client.get(
            "/v5/market/open-interest",
            {
                "category": "linear",
                "symbol": symbol,
                "intervalTime": interval_time,
                "limit": limit,
            },
        )

    def get_markets(self) -> list[dict]:
        return []
