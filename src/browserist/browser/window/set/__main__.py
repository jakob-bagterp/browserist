from .position import set_window_position
from .size import set_window_size
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods

class WindowSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def position(self, x: int, y: int) -> None:
        """Moves the window to the chosen coordinate of the screen in pixels."""

        set_window_position(self._driver, x, y)

    def size(self, x: int, y: int) -> None:
        """Restores the window and sets the window size."""

        set_window_size(self._driver, x, y)
