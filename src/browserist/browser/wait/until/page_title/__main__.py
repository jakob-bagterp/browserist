from .....constant import timeout
from .....model.browser.base.driver import BrowserDriver
from .....model.browser.base.settings import BrowserSettings
from .....model.driver_methods import DriverMethods
from .changes import wait_until_page_title_changes
from .contains import wait_until_page_title_contains
from .equals import wait_until_page_title_equals


class WaitUntilPageTitleDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def changes(self, baseline_text: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title changes from a baseline text, e.g. after a page reload or change. The text is evaluated as an exact match."""

        wait_until_page_title_changes(self._driver, baseline_text, timeout)

    def contains(self, page_title_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input can contain both a fragment or the full page title."""

        wait_until_page_title_contains(self._driver, page_title_fragment, timeout)

    def equals(self, page_title: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input has to match the exact page title."""

        wait_until_page_title_equals(self._driver, page_title, timeout)
