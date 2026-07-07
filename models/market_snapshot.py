from dataclasses import dataclass, field

from models.candle import Candle


@dataclass(slots=True)
class MarketSnapshot:
    symbol: str
    current_price: float
    low_30d: float
    distance: float = 0.0
    volume_24h: float = 0.0
    turnover_24h: float = 0.0
    funding_rate: float = 0.0
    open_interest: float = 0.0
    max_leverage: float = 0.0
    rsi: float = 0.0
    ema20: float = 0.0
    ema50: float = 0.0
    atr: float = 0.0
    macd: float = 0.0
    score: float = 0.0
    is_qualified: bool = False
    candles: list[Candle] = field(default_factory=list)
