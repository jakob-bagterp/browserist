def add_percent(value: float, tolerance_percent: float) -> float:
    """Increases a value by a given percentage."""

    return value * (1 + convert_percent_to_float(tolerance_percent))


def deduct_percent(value: float, tolerance_percent: float) -> float:
    """Decreases a value by a given percentage."""

    return value * (1 - convert_percent_to_float(tolerance_percent))


def convert_percent_to_float(tolerance_percent: float) -> float:
    return tolerance_percent / 100
