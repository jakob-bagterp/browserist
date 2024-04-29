from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .height import get_viewport_height
from .size import get_viewport_size
from .width import get_viewport_width


class ViewportGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def height(self) -> int:  # type: ignore
        """Get height of the viewport in pixels.

        Returns:
            Height of the viewport in pixels.

        Example:
            ```python title=""
            viewport_height = browser.viewport.get.height()
            ```
        """

        if self._timeout_should_continue():
            return get_viewport_height(self._browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get width and height of the viewport in pixels.

        Returns:
            Width and height of the viewport in pixels.

        Example:
            ```python title=""
            viewport_width, viewport_height = browser.viewport.get.size()
            ```
        """

        if self._timeout_should_continue():
            return get_viewport_size(self._browser_driver)

    def width(self) -> int:  # type: ignore
        """Get width of the viewport in pixels.

        Returns:
            Width of the viewport in pixels.

        Example:
            ```python title=""
            viewport_width = browser.viewport.get.width()
            ```
        """

        if self._timeout_should_continue():
            return get_viewport_width(self._browser_driver)
