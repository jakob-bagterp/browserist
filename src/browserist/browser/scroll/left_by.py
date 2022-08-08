from ...model.browser.base.driver import BrowserDriver
from .by import scroll_by


def scroll_left_by(browser_driver: BrowserDriver, pixels: int, delay_seconds: float) -> None:
    scroll_by(browser_driver, -abs(pixels), 0, delay_seconds)
