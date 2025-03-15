from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .position import get_scroll_position
from .total_height import get_total_scroll_height
from .total_width import get_total_scroll_width


class ScrollGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def position(self) -> tuple[int, int]:  # type: ignore
        """Get scroll position of the X and Y axis.

        Returns:
            Scroll position of the X and Y axis. In pixels.

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
            Total scroll height.

        Example:
            ```python title=""
            total_scroll_height = browser.scroll.get.total_height()
            ```
        """

        if self._timeout_should_continue():
            return get_total_scroll_height(self._browser_driver)

    def total_width(self) -> int:  # type: ignore
        """Get total scroll width.

        Returns:
            Total scroll width.

        Example:
            ```python title=""
            total_scroll_width = browser.scroll.get.total_width()
            ```
        """

        if self._timeout_should_continue():
            return get_total_scroll_width(self._browser_driver)
