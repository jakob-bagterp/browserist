from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .all import get_all_window_handles
from .count import count_window_handles
from .current import get_current_window_handle


class WindowHandleDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def all(self) -> list[str]:
        """Get list of IDs of all open tabs or windows."""

        return get_all_window_handles(self._driver)

    def count(self) -> int:
        """Count number of open tabs or windows."""

        return count_window_handles(self._driver)

    def current(self) -> str:
        """Get the ID of the current tab or window.

        Example: CDwindow-69663F4BF867CC38F6AF46D55BFC1A8A"""

        return get_current_window_handle(self._driver)
