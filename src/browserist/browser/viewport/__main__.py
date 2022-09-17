from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from ...model.viewport.device import DeviceViewport
from .get_size import get_viewport_size
from .height import get_screen_height
from .set_size import set_screen_size
from .set_size_by_device import set_screen_size_by_device
from .width import get_screen_width


class ViewportDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def get_size(self) -> tuple[int, int]:  # type: ignore
        """Get inner width and height of the viewport in pixels. Usage:

        width, height = browser.viewport.get_size()"""

        if self._timeout_should_continue():
            return get_viewport_size(self._browser_driver)

    def height(self) -> int:  # type: ignore
        """Get inner height of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_screen_height(self._browser_driver)

    def set_size(self, width: int, height: int) -> None:
        """Attempt to set custom viewport size in pixels.

        Note that it's recommended to run emulations in headless mode as an open browser may have minimum and maximum dimensions, either limited by the browser window or the monitor."""

        if self._timeout_should_continue():
            return set_screen_size(self._browser_driver, width, height)

    def set_size_by_device(self, device: DeviceViewport) -> None:
        """Attempt to set the viewport size by device types, e.g. iPhone, iPad or other common devices.

        Note that it's recommended to run emulations in headless mode as an open browser may have minimum and maximum dimensions, either limited by the browser window or the monitor."""

        if self._timeout_should_continue():
            return set_screen_size_by_device(self._browser_driver, device)

    def width(self) -> int:  # type: ignore
        """Get inner width of the viewport in pixels."""

        if self._timeout_should_continue():
            return get_screen_width(self._browser_driver)
