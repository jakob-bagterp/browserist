from ....model.browser.base.driver import BrowserDriver
from ...screen.height import get_screen_height
from ..by import scroll_by


def scroll_page_down(browser_driver: BrowserDriver, delay_seconds: float) -> None:
    screen_height = get_screen_height(browser_driver)
    y_scroll_pixels = screen_height + 1
    scroll_by(browser_driver, 0, y_scroll_pixels, delay_seconds)
