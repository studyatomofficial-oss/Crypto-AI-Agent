def calculate_atr(highs: list[float], lows: list[float], closes: list[float], period: int = 14) -> list[float]:
    if not highs or not lows or not closes:
        return []

    tr_values = []
    for i in range(1, len(closes)):
        high_low = highs[i] - lows[i]
        high_close = abs(highs[i] - closes[i - 1])
        low_close = abs(lows[i] - closes[i - 1])
        tr_values.append(max(high_low, high_close, low_close))

    if len(tr_values) < period:
        return [0.0] * len(closes)

    atr = [0.0] * len(closes)
    atr[period] = sum(tr_values[:period]) / period
    for i in range(period + 1, len(closes)):
        atr[i] = ((atr[i - 1] * (period - 1)) + tr_values[i - 1]) / period
    return atr
