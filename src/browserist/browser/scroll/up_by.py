from .by import scroll_by


def scroll_up_by(driver: object, pixels: int) -> None:
    scroll_by(driver, 0, -abs(pixels))
