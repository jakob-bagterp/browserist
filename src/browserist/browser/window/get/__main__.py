from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .position import get_window_position
from .size import get_window_size


class WindowGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def position(self) -> tuple[int, int]:  # type: ignore
        """Get the coordinates of the top left corner of the browser window on the screen. Usage:

        x, y = browser.window.get.position()"""

        if self._timeout_should_continue():
            return get_window_position(self._browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get width and height of browser window on the screen in pixels. Usage:

        width, height = browser.window.get.size()"""

        if self._timeout_should_continue():
            return get_window_size(self._browser_driver)
