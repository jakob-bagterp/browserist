from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .height import get_viewport_height
from .size import get_viewport_size
from .width import get_viewport_width


class ViewportGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def height(self) -> int:  # type: ignore
        """Get height of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_viewport_height(self._browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get width and height of the viewport in pixels. Usage:

        width, height = browser.viewport.get.size()"""

        if self._timeout_should_continue():
            return get_viewport_size(self._browser_driver)

    def width(self) -> int:  # type: ignore
        """Get width of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_viewport_width(self._browser_driver)
