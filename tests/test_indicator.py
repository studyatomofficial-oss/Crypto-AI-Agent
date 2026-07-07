from indicators.rsi import calculate_rsi
from indicators.ema import EMA
from models.candle import Candle
from models.market_snapshot import MarketSnapshot


def test_calculate_rsi_returns_expected_length() -> None:
    prices = [10, 11, 12, 13, 14]
    values = calculate_rsi(prices, period=2)
    assert len(values) == len(prices)


def test_ema_indicator_populates_snapshot_fields() -> None:
    snapshot = MarketSnapshot(symbol="TESTUSDT", current_price=20.0, low_30d=10.0)
    candles = [
        Candle(timestamp=i, open=20.0, high=20.0, low=20.0, close=20.0, volume=1.0, turnover=1.0)
        for i in range(25)
    ]

    EMA(20).calculate(snapshot, candles)

    assert snapshot.ema20 == 20.0
