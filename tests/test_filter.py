from services.filter_service import FilterService


def test_filter_service_returns_input() -> None:
    service = FilterService()
    data = [{"symbol": "BTCUSDT", "score": 1.0}]
    assert service.apply(data) == data
