from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from ....model.window.controller import WindowHandleController
from .new import open_new_window
from .new_tab import open_new_tab


class WindowOpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings, controller: WindowHandleController) -> None:
        super().__init__(browser_driver, settings)
        self._controller = controller

    def new(self, url: str | None = None, name: str | None = None) -> None:
        """Open and switch to new window. The URL and name of the window are optional arguments.

        name: Can be used to switch to this window with the "browser.window.switch_to(name)" method."""

        open_new_window(self._driver, self._controller, url, name)

    def new_tab(self, url: str | None = None, name: str | None = None) -> None:
        """Open and switch to new tab in current window. The URL and name of the tab are optional arguments.

        name: Can be used to switch to this tab with the "browser.window.switch_to(name)" method."""

        open_new_tab(self._driver, self._controller, url, name)
