from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .position import get_scroll_position
from .total_height import get_total_scroll_height


class ScrollGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def position(self) -> tuple[int, int]:  # type: ignore
        """Get scroll position of the X and Y axis.

        Returns:
            tuple[int, int]: Scroll position of the X and Y axis. In pixels.

        Example:
            ```python title=""
            x, y = browser.scroll.get.position()
            ```
        """

        if self._timeout_should_continue():
            return get_scroll_position(self._browser_driver)

    def total_height(self) -> int:  # type: ignore
        """Get total scroll height.

        Returns:
            int: Total scroll height.
        """

        if self._timeout_should_continue():
            return get_total_scroll_height(self._browser_driver)
