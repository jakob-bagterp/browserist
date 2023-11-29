def deduct(value: float, tolerance_percent: float) -> float:
    tolerance_as_float = tolerance_percent / 100
    return value * (1 - tolerance_as_float)
