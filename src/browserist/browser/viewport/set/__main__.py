from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from ....model.viewport.device import DeviceViewportSize
from .size import set_viewport_size
from .size_by_device import set_viewport_size_by_device


class ViewportSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def size(self, width: int, height: int) -> None:
        """Attempt to set custom viewport size in pixels.

        Note:
            It's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

        Args:
            width (int): Viewport width in pixels.
            height (int): Viewport height in pixels.
        """

        if self._timeout_should_continue():
            return set_viewport_size(self._browser_driver, width, height)

    def size_by_device(self, device: DeviceViewportSize) -> None:
        """Attempt to set the viewport size by device types, e.g. iPhone, iPad, or other common devices.

        Note:
            It's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

        Args:
            device (DeviceViewportSize): Device type to emulate.

        Example:
            ```python title="" linenums="1"
            from browserist import Browser, DeviceViewportSize

            browser = Browser()
            custom_device = DeviceViewportSize(width=375, height=812)
            browser.viewport.set.size_by_device(custom_device)
            ```
        """

        if self._timeout_should_continue():
            return set_viewport_size_by_device(self._browser_driver, device)
