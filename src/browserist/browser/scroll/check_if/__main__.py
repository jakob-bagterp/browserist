from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .is_end_of_page import check_if_scroll_is_end_of_page
from .is_top_of_page import check_if_scroll_is_top_of_page


class ScrollCheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def is_end_of_page(self) -> bool:
        """Check if current scroll position is at the end of the page."""

        return check_if_scroll_is_end_of_page(self._driver)

    def is_top_of_page(self) -> bool:
        """Check if current scroll position is at the top of the page."""

        return check_if_scroll_is_top_of_page(self._driver)
