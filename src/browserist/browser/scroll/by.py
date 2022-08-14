import time

from ...model.browser.base.driver import BrowserDriver


def scroll_by(browser_driver: BrowserDriver, x: int, y: int, delay_seconds: float) -> None:
    driver = browser_driver.get_webdriver()
    driver.execute_script(f"window.scrollBy({x}, {y});")  # type: ignore
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
