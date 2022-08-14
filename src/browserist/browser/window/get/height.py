from ....model.browser.base.driver import BrowserDriver


def get_window_height(browser_driver: BrowserDriver) -> int:
    driver = browser_driver.get_webdriver()
    return int(driver.get_window_size().get("height"))  # type: ignore
