from indicators.rsi import calculate_rsi


def test_calculate_rsi_returns_expected_length() -> None:
    prices = [10, 11, 12, 13, 14]
    values = calculate_rsi(prices, period=2)
    assert len(values) == len(prices)
