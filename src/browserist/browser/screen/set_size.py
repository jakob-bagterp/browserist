from ...model.browser.base.driver import BrowserDriver
from ..window.set.size import set_window_size
from .get_size import get_screen_size


def set_screen_size(browser_driver: BrowserDriver, width: int, height: int) -> None:
    # 1st pass:
    set_window_size(browser_driver, width, height)

    # 2nd pass if 1st pass doesn't match:
    width_check, height_check = get_screen_size(browser_driver)
    if width != width_check or height != height_check:
        width_adjusted = width + (width - width_check)
        height_adjusted = height + (height - height_check)
        set_window_size(browser_driver, width_adjusted, height_adjusted)
