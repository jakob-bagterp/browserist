from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .changes import wait_until_url_changes
from .contains import wait_until_url_contains
from .equals import wait_until_url_equals


class WaitUntilUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def changes(self, baseline_url: str, timeout: float | None = None) -> None:
        """Wait until the browser URL has changed from a baseline URL, e.g. after a redirect or form action. The URL is evaluated as an exact match."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_changes(self._browser_driver, baseline_url, timeout)

    def contains(self, url_fragment: str, timeout: float | None = None) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_contains(self._browser_driver, url_fragment, timeout)

    def equals(self, url: str, timeout: float | None = None) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL is evaluated as an exact match."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_equals(self._browser_driver, url, timeout)
