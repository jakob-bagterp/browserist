from ....model.window.controller import WindowHandleController
from .all import get_all_window_handles


def count_window_handles(driver: object, controller: WindowHandleController, selenium: bool = False) -> int:
    if selenium:
        return len(get_all_window_handles(driver, controller, selenium=True))
    else:
        return controller.count()
