from ...screen.height import get_screen_height
from ..by import scroll_by


def scroll_page_up(driver: object, delay_seconds: float) -> None:
    screen_height = get_screen_height(driver)
    y_scroll_pixels = -(screen_height + 1)
    scroll_by(driver, 0, y_scroll_pixels, delay_seconds)
