from ....model.browser.base.driver import BrowserDriver
from ..get.width import get_viewport_width
from .size import set_viewport_size


def set_viewport_height(browser_driver: BrowserDriver, height: int) -> None:
    width = get_viewport_width(browser_driver)
    set_viewport_size(browser_driver, width, height)
