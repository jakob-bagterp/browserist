from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from ...model.screen_size.device import DeviceScreenSize
from .get_size import get_screen_size
from .height import get_screen_height
from .set_size import set_screen_size
from .set_size_by_device import set_screen_size_by_device
from .width import get_screen_width


class ScreenSizeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def get_size(self) -> tuple[int, int]:  # type: ignore
        """Get inner width and height of the screen in pixels. Usage:

        width, height = browser.screen.get_size()"""

        if self._timeout_should_continue():
            return get_screen_size(self._browser_driver)

    def height(self) -> int:  # type: ignore
        """Get inner height of the screen in pixels."""

        if self._timeout_should_continue():
            return get_screen_height(self._browser_driver)

    def set_size(self, width: int, height: int) -> None:
        """When the inner screen size doesn't have the same dimensions as the outer window size, this attempts to set the screen size."""

        if self._timeout_should_continue():
            return set_screen_size(self._browser_driver, width, height)

    def set_size_by_device(self, device: DeviceScreenSize) -> None:
        """Attempt to set the screen size by device types, e.g. iPhone, iPad or other common devices, for emulation."""

        if self._timeout_should_continue():
            return set_screen_size_by_device(self._browser_driver, device)

    def width(self) -> int:  # type: ignore
        """Get inner width of the screen in pixels."""

        if self._timeout_should_continue():
            return get_screen_width(self._browser_driver)
