import time

from ....constant import timeout
from ...screen.height import get_screen_height
from ..by import scroll_by


def scroll_page_up(driver: object, delay: float = timeout.VERY_SHORT) -> None:
    screen_height = get_screen_height(driver)
    y_scroll_pixels = -(screen_height + 1)
    scroll_by(driver, 0, y_scroll_pixels)
    time.sleep(delay)  # Small delay in seconds to ensure the view is updated.
