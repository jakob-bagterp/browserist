from ...model.browser.base.driver import BrowserDriver
from .height import get_viewport_height
from .width import get_screen_width


def get_viewport_size(browser_driver: BrowserDriver) -> tuple[int, int]:
    width = get_screen_width(browser_driver)
    height = get_viewport_height(browser_driver)
    return width, height
