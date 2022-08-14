from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .is_end_of_page import check_if_scroll_is_end_of_page
from .is_top_of_page import check_if_scroll_is_top_of_page


class ScrollCheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def is_end_of_page(self) -> bool:  # type: ignore
        """Check if current scroll position is at the end of the page."""

        if self._timeout_should_continue():
            return check_if_scroll_is_end_of_page(self._browser_driver)

    def is_top_of_page(self) -> bool:  # type: ignore
        """Check if current scroll position is at the top of the page."""

        if self._timeout_should_continue():
            return check_if_scroll_is_top_of_page(self._browser_driver)
