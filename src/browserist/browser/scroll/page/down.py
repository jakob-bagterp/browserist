import time

from ....constant import timeout
from ...screen.height import get_screen_height
from ..by import scroll_by


def scroll_page_down(driver: object) -> None:
    screen_height = get_screen_height(driver)
    y_scroll_pixels = screen_height + 1
    scroll_by(driver, 0, y_scroll_pixels)
    time.sleep(timeout.VERY_SHORT)  # Small delay to ensure the view is updated.
