from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .height import set_window_height
from .position import set_window_position
from .size import set_window_size
from .width import set_window_width


class WindowSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def height(self, height: int) -> None:
        """If possible, restore the window and set the window height.

        Note:
            Window size is not the same as the [viewport size](../../../settings/viewport.md). The viewport is often smaller than the browser window that needs space for menus and buttons.

        Args:
            height (int): Height of the window in pixels.

        Example:
            ```python title=""
            browser.window.set.height(600)
            ```
        """

        if self._timeout_should_continue():
            set_window_height(self._browser_driver, height)

    def position(self, x: int, y: int) -> None:
        """If possible, move the window to the chosen coordinate of the screen.

        Args:
            x (int): In pixels. Absolute X coordinate of the screen on the horisontal axis.
            y (int): In pixels. Absolute Y coordinate of the screen on the vertical axis.

        Example:
            How to set the absolute position of the window to 100 pixels from the left and 100 pixels from the top of the screen, if possible:

            ```python linenums="1" hl_lines="4"
            from browserist import Browser

            with Browser() as browser:
                browser.window.set.position(100, 100)
                browser.open.url("https://example.com")
            ```
        """

        if self._timeout_should_continue():
            set_window_position(self._browser_driver, x, y)

    def size(self, width: int, height: int) -> None:
        """If possible, restore the window and set the window size.

        Note:
            Window size is not the same as the [viewport size](../../../settings/viewport.md). The viewport is often smaller than the browser window that needs space for menus and buttons.

        Args:
            width (int): Width of the window in pixels.
            height (int): Height of the window in pixels.

        Example:
            ```python title=""
            browser.window.set.size(800, 600)
            ```
        """

        if self._timeout_should_continue():
            set_window_size(self._browser_driver, width, height)

    def width(self, width: int) -> None:
        """If possible, restore the window and set the window width.

        Note:
            Window size is not the same as the [viewport size](../../../settings/viewport.md). The viewport is often smaller than the browser window that needs space for menus and buttons.

        Args:
            width (int): Width of the window in pixels.

        Example:
            ```python title=""
            browser.window.set.width(800)
            ```
        """

        if self._timeout_should_continue():
            set_window_width(self._browser_driver, width)
