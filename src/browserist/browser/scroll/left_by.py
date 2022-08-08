from .by import scroll_by


def scroll_left_by(driver: object, pixels: int, delay_seconds: float) -> None:
    scroll_by(driver, -abs(pixels), 0, delay_seconds)
