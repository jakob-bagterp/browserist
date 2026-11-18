from ....model.browser.base.driver import BrowserDriver
from ..get.position import get_scroll_position
from ..get.total_height import get_total_scroll_height
from ..to_position import scroll_to_position


def scroll_to_end_of_page(browser_driver: BrowserDriver, delay_seconds: float) -> None:
    x, _ = get_scroll_position(browser_driver)
    y_end = get_total_scroll_height(browser_driver)
    scroll_to_position(browser_driver, x, y_end, delay_seconds)
