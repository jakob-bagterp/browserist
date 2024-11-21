from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .height import get_window_height
from .position import get_window_position
from .size import get_window_size
from .width import get_window_width


class WindowGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def height(self) -> int:  # type: ignore
        """Get the height of browser window on the screen in pixels.

        Returns:
            Height of browser window on the screen in pixels.

        Example:
            ```python title=""
            height = browser.window.get.height()
            ```
        """

        if self._timeout_should_continue():
            return get_window_height(self._browser_driver)

    def position(self) -> tuple[int, int]:  # type: ignore
        """Get the X and Y coordinates of the top left corner of the browser window on the screen.

        Returns:
            Coordinates of the top left corner of the browser window on the screen.

        Example:
            How to move the window relatively by getting the current position of the window and move it by 10 pixels in both axes, if possible:

            ```python linenums="1" hl_lines="4"
            from browserist import Browser

            with Browser() as browser:
                x, y = browser.window.get.position()
                browser.window.set.position(x - 10, y - 10)
                browser.open.url("https://example.com")
            ```
        """

        if self._timeout_should_continue():
            return get_window_position(self._browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get width and height of browser window on the screen in pixels.

        Returns:
            Width and height of browser window on the screen in pixels.

        Example:
            ```python title=""
            width, height = browser.window.get.size()
            ```
        """

        if self._timeout_should_continue():
            return get_window_size(self._browser_driver)

    def width(self) -> int:  # type: ignore
        """Get the width of browser window on the screen in pixels.

        Returns:
            Width of browser window on the screen in pixels.

        Example:
            ```python title=""
            width = browser.window.get.width()
            ```
        """

        if self._timeout_should_continue():
            return get_window_width(self._browser_driver)
