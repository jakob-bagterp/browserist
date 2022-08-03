from ....model.browser.base.driver import BrowserDriver


def get_window_position(browser_driver: BrowserDriver) -> tuple[int, int]:
    driver = browser_driver.get_webdriver()
    x = int(driver.get_window_position().get("x"))  # type: ignore
    y = int(driver.get_window_position().get("y"))  # type: ignore
    return x, y
