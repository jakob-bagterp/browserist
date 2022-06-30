from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .position import get_scroll_position
from .total_height import get_total_scroll_height


class ScrollGetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def position(self) -> tuple[int, int]:
        """Get scroll position of the X and Y axis. Usage:

        x, y = browser.scroll.get.position()"""

        return get_scroll_position(self._driver)

    def total_height(self) -> int:
        """Get total scroll height."""

        return get_total_scroll_height(self._driver)
