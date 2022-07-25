from .....model.browser.base.driver import BrowserDriver
from .....model.browser.base.settings import BrowserSettings
from .....model.driver_methods import DriverMethods
from .changes import wait_until_text_changes
from .contains import wait_until_text_contains
from .equals import wait_until_text_equals


class WaitUntilTextDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def changes(self, xpath: str, baseline_text: str, timeout: int | None = None) -> None:
        """Wait until the text of an element changes from a baseline text, e.g. after a form action. The text is evaluated as an exact match."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_changes(self._driver, self._settings, xpath, baseline_text, timeout)

    def contains(self, xpath: str, regex: str, timeout: int | None = None) -> None:
        """Wait until the text of an element has changed, e.g. after a form action."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_contains(self._driver, self._settings, xpath, regex, timeout)

    def equals(self, xpath: str, regex: str, timeout: int | None = None) -> None:
        """Wait until the text of an element has changed, e.g. after a form action. The text is evaluated as an exact match."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_equals(self._driver, self._settings, xpath, regex, timeout)
