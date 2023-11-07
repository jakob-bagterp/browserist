from ...model.browser.base.driver import BrowserDriver


def get_page_title(browser_driver: BrowserDriver) -> str:
    driver = browser_driver.get_webdriver()
    return driver.title
