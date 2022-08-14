from ....model.browser.base.driver import BrowserDriver


def get_scroll_position(browser_driver: BrowserDriver) -> tuple[int, int]:
    driver = browser_driver.get_webdriver()
    x = int(driver.execute_script("return window.pageXOffset;"))  # type: ignore
    y = int(driver.execute_script("return window.pageYOffset;"))  # type: ignore
    return x, y
