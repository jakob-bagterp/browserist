from ...model.browser.base.driver import BrowserDriver


def window_maximize(browser_driver: BrowserDriver) -> None:
    driver = browser_driver.get_webdriver()
    driver.maximize_window()
