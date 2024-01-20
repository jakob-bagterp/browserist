from ...model.browser.base.driver import BrowserDriver


def window_minimize(browser_driver: BrowserDriver) -> None:
    driver = browser_driver.get_webdriver()
    driver.minimize_window()
