from ...model.browser.base.driver import BrowserDriver


def window_fullscreen(browser_driver: BrowserDriver) -> None:
    driver = browser_driver.get_webdriver()
    driver.fullscreen_window()
