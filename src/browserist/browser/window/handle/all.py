from ....model.browser.base.driver import BrowserDriver
from ....model.window.controller import WindowHandleController


def get_all_window_handles(browser_driver: BrowserDriver, controller: WindowHandleController, selenium: bool = False) -> list[str]:
    if not selenium:
        return [window_handle.id for window_handle in controller._window_handles]
    driver = browser_driver.get_webdriver()
    return driver.window_handles
