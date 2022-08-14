from ....model.browser.base.driver import BrowserDriver


def get_window_size(browser_driver: BrowserDriver) -> tuple[int, int]:
    driver = browser_driver.get_webdriver()
    width = int(driver.get_window_size().get("width"))  # type: ignore
    height = int(driver.get_window_size().get("height"))  # type: ignore
    return width, height
