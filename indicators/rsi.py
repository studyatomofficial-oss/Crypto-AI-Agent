def calculate_rsi(prices: list[float], period: int = 14) -> list[float]:
    if not prices:
        return []
    if len(prices) < 2:
        return [0.0]

    deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [max(delta, 0) for delta in deltas]
    losses = [abs(min(delta, 0)) for delta in deltas]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    rsi_values = [0.0] * len(prices)

    if avg_loss == 0:
        return [100.0] * len(prices)

    rs = avg_gain / avg_loss
    rsi_values[period] = 100 - (100 / (1 + rs))

    for i in range(period + 1, len(prices)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i - 1]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i - 1]) / period
        rs = avg_gain / avg_loss
        rsi_values[i] = 100 - (100 / (1 + rs))

    return rsi_values
