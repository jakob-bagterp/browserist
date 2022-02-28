from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .get_position import get_scroll_position
from .into_view import scroll_into_view
from .into_view_if_not_visible import scroll_into_view_if_not_visible
from .to_end_of_page import scroll_to_end_of_page
from .to_position import scroll_to_position
from .to_top_of_page import scroll_to_top_of_page


class ScrollDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def get_position(self) -> tuple[int, int]:
        """Get scroll position of the X and Y axis. Usage:

        x, y = browser.scroll.get_position()"""

        return get_scroll_position(self._driver)

    def into_view(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Find element and scroll up or down until element is visible."""

        scroll_into_view(self._driver, xpath, timeout)

    def into_view_if_not_visible(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """If not visilbe, find element and scroll up or down until element is visible."""

        scroll_into_view_if_not_visible(self._driver, xpath, timeout)

    def to_end_of_page(self) -> None:
        """Scroll to end of page."""

        scroll_to_end_of_page(self._driver)

    def to_position(self, x: int, y: int) -> None:
        """Scroll to coordinate X and Y pixels of page."""

        scroll_to_position(self._driver, x, y)

    def to_top_of_page(self) -> None:
        """Scroll to top of page."""

        scroll_to_top_of_page(self._driver)
