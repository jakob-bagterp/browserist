from ...model.browser.base.driver import BrowserDriver
from ...model.window.controller import WindowHandleController
from .handle.current import get_current_window_handle


def window_close(browser_driver: BrowserDriver, controller: WindowHandleController) -> None:
    current_window_handle_id = get_current_window_handle(browser_driver)
    controller.remove_handle_by_id(current_window_handle_id)
    driver = browser_driver.get_webdriver()
    driver.close()
