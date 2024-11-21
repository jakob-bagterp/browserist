from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from ....model.viewport.device import DeviceViewportSize
from .height import set_viewport_height
from .size import set_viewport_size
from .size_by_device import set_viewport_size_by_device
from .width import set_viewport_width


class ViewportSetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def height(self, height: int) -> None:
        """Attempt to set custom viewport height in pixels.

        Note:
            It's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

        Args:
            height (int): Viewport height in pixels.

        Example:
            ```python title=""
            browser.viewport.set.height(1080)
            ```
        """

        if self._timeout_should_continue():
            return set_viewport_height(self._browser_driver, height)

    def size(self, width: int, height: int) -> None:
        """Attempt to set custom viewport size in pixels.

        Note:
            It's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

        Args:
            width (int): Viewport width in pixels.
            height (int): Viewport height in pixels.

        Example:
            ```python title=""
            browser.viewport.set.size(1920, 1080)
            ```
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
            ```python title="" linenums="1" hl_lines="4-5"
            from browserist import Browser, DeviceViewportSize

            with Browser() as browser:
                custom_device = DeviceViewportSize(width=375, height=812)
                browser.viewport.set.size_by_device(custom_device)
            ```
        """

        if self._timeout_should_continue():
            return set_viewport_size_by_device(self._browser_driver, device)

    def width(self, width: int) -> None:
        """Attempt to set custom viewport width in pixels.

        Note:
            It's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

        Args:
            width (int): Viewport width in pixels.

        Example:
            ```python title=""
            browser.viewport.set.width(1920)
            ```
        """

        if self._timeout_should_continue():
            return set_viewport_width(self._browser_driver, width)
