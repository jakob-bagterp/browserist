from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .switch_to import switch_to_iframe
from .switch_to_original_page import switch_to_original_page


class IframeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def switch_to(self, xpath: str, timeout: float | None = None) -> None:
        """Switch to iframe.

        Args:
            xpath (str): XPath of the iframe.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            switch_to_iframe(self._browser_driver, xpath, timeout)

    def switch_to_original_page(self) -> None:
        """After switch to iframe, use this to come back to the original page."""

        if self._timeout_should_continue():
            switch_to_original_page(self._browser_driver)
