from .by import scroll_by


def scroll_down_by(driver: object, pixels: int) -> None:
    scroll_by(driver, 0, abs(pixels), 1)  # TODO: Add delay_seconds=1.
