from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .for_element import wait_for_element
from .random_seconds import wait_random_seconds
from .seconds import wait_seconds
from .until.__main__ import WaitUntilDriverMethods


class WaitDriverMethods(DriverMethods):
    __slots__ = ["until"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.until: WaitUntilDriverMethods = WaitUntilDriverMethods(browser_driver)

    def for_element(self, xpath: str, timeout: float | None = None) -> None:
        """Wait until element on the current page is ready in the DOM and/or on the screen.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            Useful for single-page application elements handled by JavaScript, but also for standard HTML that doesn't load immediately. This helper function ensures that DOM elements are ready before processing. The example waits for any H1 heading to be ready:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.for_element("//h1")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_for_element(self._browser_driver, xpath, timeout)

    def random_seconds(self, min_seconds: float = 1, max_seconds: float = 5) -> None:
        """Sleep for a random amount of time to make actions look less like a bot. The waiting time will be somewhere between the speficied minimum and maximum seconds.

        Args:
            min_seconds (float, optional): Minimum seconds to wait.
            max_seconds (float, optional): Maximum seconds to wait.

        Example:
            For example, wait between 3 and 20 seconds:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.random_seconds(3, 20)
            ```
        """

        if self._timeout_should_continue():
            wait_random_seconds(min_seconds, max_seconds)

    def seconds(self, seconds: float) -> None:
        """Sleep for a fixed amount of time.

        Args:
            seconds (float): Seconds to wait.

        Example:
            For example, wait for 5 seconds:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.seconds(5)
            ```
        """

        if self._timeout_should_continue():
            wait_seconds(seconds)
