import time

from ...constant import timeout
from ..get.screen.height import get_screen_height
from .get_position import get_scroll_position
from .to_position import scroll_to_position


def scroll_page_down(driver: object) -> None:
    current_position_x, current_position_y = get_scroll_position(driver)
    screen_height_x = get_screen_height(driver)
    page_down_position_x = current_position_x + screen_height_x + 1
    scroll_to_position(driver, page_down_position_x, current_position_y)
    time.sleep(timeout.VERY_SHORT)  # Small delay to ensure the view is updated.
