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
    crash_score: float = 0.0
    accumulation_score: float = 0.0
    accumulation_days: int = 0
    compression_score: float = 0.0
    bottom_stability_score: float = 0.0
    recovery_percent: float = 0.0
    recovery_score: float = 0.0
    range_score: float = 0.0
    sleeping_score: float = 0.0
    is_qualified: bool = False
    high_90d: float = 0.0
    crash_percent: float = 0.0
    high_30d: float = 0.0
    compression_percent: float = 0.0
    bottom_stability_percent: float = 0.0
    position_in_range: float = 0.0
    days_near_bottom: int = 0
    bottom_zone_percent: float = 5.0
    volume_dryup_percent: float = 0.0
    candles: list[Candle] = field(default_factory=list)
