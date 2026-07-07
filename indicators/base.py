from abc import ABC, abstractmethod

from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class Indicator(ABC):
    @abstractmethod
    def calculate(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        pass
