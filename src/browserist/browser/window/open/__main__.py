from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .new import open_new_window
from .new_tab import open_new_tab


class WindowOpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def new(self, url: str | None = None) -> None:
        """Open and switch to new window. The URL argument is optional."""

        open_new_window(self._driver, url)

    def new_tab(self, url: str | None = None) -> None:
        """Open and switch to new tab in current window. The URL argument is optional."""

        open_new_tab(self._driver, url)
