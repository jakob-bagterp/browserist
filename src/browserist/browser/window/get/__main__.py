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
            int: Height of browser window on the screen in pixels.
        """

        if self._timeout_should_continue():
            return get_window_height(self._browser_driver)

    def position(self) -> tuple[int, int]:  # type: ignore
        """Get the X and Y coordinates of the top left corner of the browser window on the screen.

        Returns:
            tuple[int, int]: Coordinates of the top left corner of the browser window on the screen.

        Example:
            ```python title=""
            x, y = browser.window.get.position()
            ```
        """

        if self._timeout_should_continue():
            return get_window_position(self._browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get width and height of browser window on the screen in pixels.

        Returns:
            tuple[int, int]: Width and height of browser window on the screen in pixels.

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
            int: Width of browser window on the screen in pixels.
        """

        if self._timeout_should_continue():
            return get_window_width(self._browser_driver)
