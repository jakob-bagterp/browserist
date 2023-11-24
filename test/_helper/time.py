def deduct_tolerance(time: float, tolerance_percent: float) -> float:
    tolerance_as_float = tolerance_percent / 100
    return time * (1 - tolerance_as_float)


def get_difference(time_a: float, time_b: float) -> float:
    return abs(time_a - time_b)
