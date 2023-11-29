def add(value: float, tolerance_percent: float) -> float:
    return value * (1 + convert_percent_to_float(tolerance_percent))


def deduct(value: float, tolerance_percent: float) -> float:
    return value * (1 - convert_percent_to_float(tolerance_percent))


def convert_percent_to_float(tolerance_percent: float) -> float:
    return tolerance_percent / 100
