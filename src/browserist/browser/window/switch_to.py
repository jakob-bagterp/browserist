from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.window.controller import WindowHandleController


def switch_to_window(browser_driver: BrowserDriver, controller: WindowHandleController, window_handle: str) -> None:
    driver = browser_driver.get_webdriver()
    if helper.window_handle.is_valid_id(window_handle):
        driver.switch_to.window(window_handle)
    else:
        window_handle_id = controller.get_handle_id_by_name(window_handle)
        driver.switch_to.window(window_handle_id)
