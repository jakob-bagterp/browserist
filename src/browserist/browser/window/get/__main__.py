from .current_handle import get_current_window_handle
from .position import get_window_position
from .size import get_window_size
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods

class WindowGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def current_handle(self) -> str:
        """Get the ID of the current window."""

        return get_current_window_handle(self._driver)

    def position(self) -> tuple[int, int]:
        """Get the coordinates of the top left corner of the browser window on the screen. Usage:

        x, y = browser.window.get.position()"""

        return get_window_position(self._driver)

    def size(self) -> tuple[int, int]:
        """Get width and height of browser window on the screen in pixels. Usage:

        width, height = browser.window.get.size()"""

        return get_window_size(self._driver)
