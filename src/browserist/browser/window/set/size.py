from ....model.browser.base.driver import BrowserDriver


def set_window_size(browser_driver: BrowserDriver, width: int, height: int) -> None:
    driver = browser_driver.get_webdriver()
    driver.set_window_size(width, height)
