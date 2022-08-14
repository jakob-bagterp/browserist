from ....model.browser.base.driver import BrowserDriver
from .height import get_window_height
from .width import get_window_width


def get_window_size(browser_driver: BrowserDriver) -> tuple[int, int]:
    width = get_window_width(browser_driver)
    height = get_window_height(browser_driver)
    return width, height
