from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .size import set_viewport_size


class ViewportSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def size(self, width: int, height: int) -> None:
        """Attempt to set custom viewport size in pixels.

        Note that it's recommended to run emulations in headless mode as an open browser may have minimum and maximum dimensions, either limited by the browser window or the monitor."""

        if self._timeout_should_continue():
            return set_viewport_size(self._browser_driver, width, height)
