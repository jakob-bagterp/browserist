from ....model.browser.base.driver import BrowserDriver
from ..to_position import scroll_to_position


def scroll_to_top_of_page(browser_driver: BrowserDriver, delay_seconds: float) -> None:
    scroll_to_position(browser_driver, 0, 0, delay_seconds)
