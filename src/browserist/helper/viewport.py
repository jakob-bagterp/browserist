def calculate_size_adjustment(size_to_be: int, size_current: int) -> int:
    """Calculate viewport size adjustment for either width or height by assessing the difference between the size to be and the current size."""

    return size_to_be + (size_to_be - size_current)
