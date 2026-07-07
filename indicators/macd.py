def calculate_macd(prices: list[float], fast: int = 12, slow: int = 26, signal: int = 9) -> dict:
    if not prices:
        return {"macd": [], "signal": [], "histogram": []}

    from indicators.ema import calculate_ema

    fast_ema = calculate_ema(prices, fast)
    slow_ema = calculate_ema(prices, slow)
    macd_line = [fast_ema[i] - slow_ema[i] for i in range(min(len(fast_ema), len(slow_ema)))]
    signal_line = calculate_ema(macd_line, signal)
    histogram = [macd_line[i] - signal_line[i] for i in range(min(len(macd_line), len(signal_line)))]

    return {"macd": macd_line, "signal": signal_line, "histogram": histogram}
