from ...model.browser.base.driver import BrowserDriver
from .by import scroll_by


def scroll_up_by(browser_driver: BrowserDriver, pixels: int, delay_seconds: float) -> None:
    scroll_by(browser_driver, 0, -abs(pixels), delay_seconds)
