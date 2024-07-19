from ....model.browser.base.driver import BrowserDriver
from ..get.width import get_window_width
from .size import set_window_size


def set_window_height(browser_driver: BrowserDriver, height: int) -> None:
    width = get_window_width(browser_driver)
    set_window_size(browser_driver, width, height)
