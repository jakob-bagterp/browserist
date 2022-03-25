from ... import helper
from ...model.window.controller import WindowHandleController


def switch_to_window(driver: object, controller: WindowHandleController, window_handle: str) -> None:
    if helper.window_handle.is_valid_id(window_handle):
        driver.switch_to.window(window_handle)  # type: ignore
    else:
        window_handle_id = controller.get_handle_id_by_name(window_handle)
        driver.switch_to.window(window_handle_id)  # type: ignore
