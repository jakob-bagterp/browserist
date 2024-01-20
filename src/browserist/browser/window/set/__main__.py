from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .position import set_window_position
from .size import set_window_size


class WindowSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def position(self, x: int, y: int) -> None:
        """If possible, move the window to the chosen coordinate of the screen.

        Args:
            x (int): In pixels. Absolute X coordinate of the screen on the horisontal axis.
            y (int): In pixels. Absolute Y coordinate of the screen on the vertical axis.
        """

        if self._timeout_should_continue():
            set_window_position(self._browser_driver, x, y)

    def size(self, width: int, height: int) -> None:
        """If possible, restore the window and set the window size.

        Note:
            Window size is not the same as the [viewport](../../../user-guide/settings/viewport.md) size. The viewport is often smaller than the browser window that needs space for menus and buttons.

        Args:
            width (int): Width of the window in pixels.
            height (int): Height of the window in pixels.
        """

        if self._timeout_should_continue():
            set_window_size(self._browser_driver, width, height)
