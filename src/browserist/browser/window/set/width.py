from ....model.browser.base.driver import BrowserDriver
from ..get.height import get_window_height
from .size import set_window_size


def set_window_width(browser_driver: BrowserDriver, width: int) -> None:
    height = get_window_height(browser_driver)
    set_window_size(browser_driver, width, height)
