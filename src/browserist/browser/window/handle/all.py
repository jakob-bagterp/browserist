from ....model.window.controller import WindowHandleController


def get_all_window_handles(driver: object, controller: WindowHandleController, selenium: bool = False) -> list[str]:
    if selenium:
        return driver.window_handles
    else:
        return [window_handle.id for window_handle in controller._window_handles]
