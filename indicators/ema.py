from indicators.base import Indicator
from models.candle import Candle
from models.market_snapshot import MarketSnapshot


class EMA(Indicator):
    def __init__(self, period: int) -> None:
        self.period = period

    def calculate(self, snapshot: MarketSnapshot, candles: list[Candle]) -> None:
        closes = [candle.close for candle in candles]
        if not closes:
            return

        effective_period = min(self.period, len(closes))
        multiplier = 2 / (effective_period + 1)
        ema = sum(closes[:effective_period]) / effective_period
        for price in closes[effective_period:]:
            ema = (price - ema) * multiplier + ema

        if self.period == 20:
            snapshot.ema20 = ema
        elif self.period == 50:
            snapshot.ema50 = ema


def calculate_ema(values: list[float], period: int = 14) -> list[float]:
    if not values:
        return []
    if len(values) == 1:
        return [float(values[0])]

    multiplier = 2 / (period + 1)
    ema_values = [float(values[0])]
    prev_ema = float(values[0])

    for value in values[1:]:
        prev_ema = (float(value) * multiplier) + (prev_ema * (1 - multiplier))
        ema_values.append(prev_ema)

    return ema_values
