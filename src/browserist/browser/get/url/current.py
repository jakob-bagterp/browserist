from ....model.browser.base.driver import BrowserDriver


def get_current_url(browser_driver: BrowserDriver) -> str:
    driver = browser_driver.get_webdriver()
    return driver.current_url
