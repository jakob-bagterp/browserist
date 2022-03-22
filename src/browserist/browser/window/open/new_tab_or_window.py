from ....model.window.controller import WindowHandleController
from ....model.window.tab_or_window import TabOrWindow
from ...open.url import open_url
from ...wait.until_number_of_window_handles_is import wait_until_number_of_window_handles_is
from ..handle.count import count_window_handles
from ..handle.current import get_current_window_handle


def open_new_tab_or_window(driver: object,
                           controller: WindowHandleController,
                           tab_or_window: TabOrWindow,
                           url: str | None = None,
                           name: str | None = None) -> None:
    current_number_of_window_handles = count_window_handles(driver, controller, selenium=True)
    driver.switch_to.new_window(tab_or_window.value)  # type: ignore
    wait_until_number_of_window_handles_is(driver, current_number_of_window_handles + 1)
    new_handle_id = get_current_window_handle(driver)
    controller.add_handle(new_handle_id, name)
    if url:
        open_url(driver, url)
