from .....constant import timeout
from .....model.browser.base.driver import BrowserDriver
from .....model.browser.base.settings import BrowserSettings
from .....model.driver_methods import DriverMethods
from .changes import wait_until_url_changes


class WaitUntilUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def changes(self, baseline_url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed from a baseline URL, e.g. after a redirect or form action. The URL is evaluated as an exact match."""

        wait_until_url_changes(self._driver, baseline_url, timeout)
