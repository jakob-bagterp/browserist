from .... import helper
from ....model.browser.base.driver import BrowserDriver
from ....model.window.controller import WindowHandleController
from ....model.window.tab_or_window import TabOrWindow
from ...open.url import open_url
from ...wait.until.number_of_window_handles_is import wait_until_number_of_window_handles_is
from ..handle.count import count_window_handles
from ..handle.current import get_current_window_handle


def open_new_tab_or_window(
    browser_driver: BrowserDriver,
    controller: WindowHandleController,
    tab_or_window: TabOrWindow,
    timeout: float,
    url: str | None = None,
    name: str | None = None,
) -> None:
    url = helper.url.mediate_conversion_to_tiny_type_or_none(url)
    current_number_of_window_handles = count_window_handles(browser_driver, controller, selenium=True)
    driver = browser_driver.get_webdriver()
    driver.switch_to.new_window(tab_or_window.value)
    wait_until_number_of_window_handles_is(browser_driver, current_number_of_window_handles + 1, timeout)
    new_handle_id = get_current_window_handle(browser_driver)
    controller.add_handle(new_handle_id, name)
    if url:
        open_url(browser_driver, url)
