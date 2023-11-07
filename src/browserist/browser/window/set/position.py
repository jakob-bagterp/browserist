from ....model.browser.base.driver import BrowserDriver


def set_window_position(browser_driver: BrowserDriver, x: int, y: int) -> None:
    driver = browser_driver.get_webdriver()
    driver.set_window_position(x, y)
