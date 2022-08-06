from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .for_element import wait_for_element
from .random_time import wait_random_time
from .until.__main__ import WaitUntilDriverMethods


class WaitDriverMethods(DriverMethods):
    __slots__ = ["until"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.until: WaitUntilDriverMethods = WaitUntilDriverMethods(browser_driver)

    def for_element(self, xpath: str, timeout: float | None = None) -> None:
        """Wait until element is ready in the DOM and/or on the screen.

        Especially useful for single-page app elements handled/modified by JavaScript, but also standard HTML that doesn't load immediately, this helper function ensures that DOM elements are ready before processing."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_for_element(self._browser_driver, xpath, timeout)

    def random_time(self, min_seconds: float = 1, max_seconds: float = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        if self._timeout_should_continue():
            wait_random_time(min_seconds, max_seconds)
