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
