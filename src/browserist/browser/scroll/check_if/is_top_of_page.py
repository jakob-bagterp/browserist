from ....model.browser.base.driver import BrowserDriver
from ..get.position import get_scroll_position


def check_if_scroll_is_top_of_page(browser_driver: BrowserDriver) -> bool:
    _, y = get_scroll_position(browser_driver)
    return y == 0
