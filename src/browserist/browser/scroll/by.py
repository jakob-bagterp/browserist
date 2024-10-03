import time

from ...model.browser.base.driver import BrowserDriver
from ..tool.execute_script import tool_execute_script


def scroll_by(browser_driver: BrowserDriver, x: int, y: int, delay_seconds: float) -> None:
    tool_execute_script(browser_driver, f"window.scrollBy({x}, {y});")
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
