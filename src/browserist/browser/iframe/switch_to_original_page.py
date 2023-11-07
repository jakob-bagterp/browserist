from ...model.browser.base.driver import BrowserDriver


def switch_to_original_page(browser_driver: BrowserDriver) -> None:
    driver = browser_driver.get_webdriver()
    driver.switch_to.default_content()
