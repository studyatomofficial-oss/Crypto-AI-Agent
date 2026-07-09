from services.market_service import MarketService
from models.candle import Candle


def test_get_candles_returns_candle_objects(monkeypatch) -> None:
    service = MarketService()

    def fake_get_kline(symbol: str, limit: int = 30) -> dict:
        return {
            "result": {
                "list": [
                    [
                        "1783382400000",
                        "0.00432",
                        "0.00451",
                        "0.00401",
                        "0.00447",
                        "123456",
                        "98765",
                    ]
                ]
            }
        }

    monkeypatch.setattr(service.bybit, "get_kline", fake_get_kline)

    candles = service.get_candles("AGIUSDT")

    assert len(candles) == 1
    assert isinstance(candles[0], Candle)
    assert candles[0].timestamp == 1783382400000
    assert candles[0].open == 0.00432
    assert candles[0].high == 0.00451
    assert candles[0].low == 0.00401
    assert candles[0].close == 0.00447
    assert candles[0].volume == 123456.0
    assert candles[0].turnover == 98765.0


def test_get_candles_returns_empty_list_when_payload_is_missing_candles(monkeypatch) -> None:
    service = MarketService()

    def fake_get_kline(symbol: str, limit: int = 30) -> dict:
        return {"result": {}}

    monkeypatch.setattr(service.bybit, "get_kline", fake_get_kline)

    try:
        candles = service.get_candles("AGIUSDT")
        assert False, "Expected ValueError for missing candle data"
    except ValueError as e:
        assert "No candle data" in str(e)


def test_get_open_interest_series_returns_sorted_daily_values(monkeypatch) -> None:
    service = MarketService()

    def fake_get_open_interest_history(symbol: str, interval_time: str = "1d", limit: int = 31) -> dict:
        return {
            "result": {
                "list": [
                    {"openInterest": "120", "timestamp": "3000"},
                    {"openInterest": "100", "timestamp": "1000"},
                    {"openInterest": "110", "timestamp": "2000"},
                ]
            }
        }

    monkeypatch.setattr(service.bybit, "get_open_interest_history", fake_get_open_interest_history)

    series = service.get_open_interest_series("AGIUSDT")

    assert series == [100.0, 110.0, 120.0]
