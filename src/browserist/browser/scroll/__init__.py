from .into_view import scroll_into_view
from .into_view_if_not_visible import scroll_into_view_if_not_visible
from .to_end_of_page import scroll_to_end_of_page
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class ScrollDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def into_view(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Find element and scroll up or down until element is visible."""

        scroll_into_view(self._driver, xpath, timeout)

    def into_view_if_not_visible(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """If not visilbe, find element and scroll up or down until element is visible."""

        scroll_into_view_if_not_visible(self._driver, xpath, timeout)

    def to_end_of_page(self) -> None:
        """Scroll to end of page."""

        scroll_to_end_of_page(self._driver)
