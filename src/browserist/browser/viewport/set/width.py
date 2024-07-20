from ....model.browser.base.driver import BrowserDriver
from ..get.height import get_viewport_height
from .size import set_viewport_size


def set_viewport_width(browser_driver: BrowserDriver, width: int) -> None:
    height = get_viewport_height(browser_driver)
    set_viewport_size(browser_driver, width, height)
