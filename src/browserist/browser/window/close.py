from ...model.window.controller import WindowHandleController
from .handle.current import get_current_window_handle


def window_close(driver: object, controller: WindowHandleController) -> None:
    current_window_handle_id = get_current_window_handle(driver)
    controller.remove_handle_by_id(current_window_handle_id)
    driver.close()  # type: ignore
