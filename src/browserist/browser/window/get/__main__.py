from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .all_handles import get_all_window_handles
from .count_handles import count_window_handles
from .current_handle import get_current_window_handle
from .position import get_window_position
from .size import get_window_size


class WindowGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def all_handles(self) -> list[str]:
        """Get list of IDs of all open tabs or windows."""

        return get_all_window_handles(self._driver)

    def count_handles(self) -> int:
        """Count number of open tabs or windows."""

        return count_window_handles(self._driver)

    def current_handle(self) -> str:
        """Get the ID of the current tab or window."""

        return get_current_window_handle(self._driver)

    def position(self) -> tuple[int, int]:
        """Get the coordinates of the top left corner of the browser window on the screen. Usage:

        x, y = browser.window.get.position()"""

        return get_window_position(self._driver)

    def size(self) -> tuple[int, int]:
        """Get width and height of browser window on the screen in pixels. Usage:

        width, height = browser.window.get.size()"""

        return get_window_size(self._driver)
