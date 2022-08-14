from ...model.browser.base.driver import BrowserDriver


def get_screen_height(browser_driver: BrowserDriver) -> int:
    driver = browser_driver.get_webdriver()
    return int(driver.execute_script("return window.innerHeight;"))  # type: ignore
