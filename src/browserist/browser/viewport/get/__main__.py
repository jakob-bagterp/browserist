from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .size import get_viewport_size


class ViewportGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def size(self) -> tuple[int, int]:  # type: ignore
        """Get inner width and height of the viewport in pixels. Usage:

        width, height = browser.viewport.get.size()"""

        if self._timeout_should_continue():
            return get_viewport_size(self._browser_driver)
