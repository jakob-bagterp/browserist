from ..get.screen.height import get_screen_height
from .get_position import get_scroll_position
from .to_position import scroll_to_position


def scroll_page_up(driver: object) -> None:
    current_position_x, current_position_y = get_scroll_position(driver)
    screen_height_x = get_screen_height(driver)
    page_up_position_x = max(current_position_x - screen_height_x, 0)
    scroll_to_position(driver, page_up_position_x, current_position_y)
