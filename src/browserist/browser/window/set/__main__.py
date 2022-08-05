from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .position import set_window_position
from .size import set_window_size


class WindowSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def position(self, x: int, y: int) -> None:
        """Moves the window to the chosen coordinate of the screen in pixels."""

        if self._timeout_should_continue():
            set_window_position(self._browser_driver, x, y)

    def size(self, width: int, height: int) -> None:
        """Restores the window and sets the window size."""

        if self._timeout_should_continue():
            set_window_size(self._browser_driver, width, height)
