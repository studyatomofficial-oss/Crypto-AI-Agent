from typing import Dict


class MarketCache:
    def __init__(self) -> None:
        self._tickers: Dict[str, dict] = {}

    def load(self, tickers: list[dict]) -> None:
        self._tickers.clear()
        for ticker in tickers:
            self._tickers[ticker["symbol"]] = ticker

    def get(self, symbol: str) -> dict | None:
        return self._tickers.get(symbol)

    def contains(self, symbol: str) -> bool:
        return symbol in self._tickers

    def clear(self) -> None:
        self._tickers.clear()

    @property
    def size(self) -> int:
        return len(self._tickers)
