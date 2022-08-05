from ....model.browser.base.driver import BrowserDriver
from ....model.window.controller import WindowHandleController
from .all import get_all_window_handles


def count_window_handles(browser_driver: BrowserDriver, controller: WindowHandleController, selenium: bool = False) -> int:
    if selenium:
        return len(get_all_window_handles(browser_driver, controller, selenium=True))
    else:
        return controller.count()
