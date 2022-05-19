from .....constant import timeout
from .....model.browser.base.driver import BrowserDriver
from .....model.browser.base.settings import BrowserSettings
from .....model.driver_methods import DriverMethods
from .changes import wait_until_url_changes
from .contains import wait_until_url_contains
from .equals import wait_until_url_equals


class WaitUntilUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def changes(self, baseline_url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed from a baseline URL, e.g. after a redirect or form action. The URL is evaluated as an exact match."""

        wait_until_url_changes(self._driver, baseline_url, timeout)

    def contains(self, url_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        wait_until_url_contains(self._driver, url_fragment, timeout)

    def equals(self, url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL is evaluated as an exact match."""

        wait_until_url_equals(self._driver, url, timeout)
