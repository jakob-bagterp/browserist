from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .changes import wait_until_text_changes
from .contains import wait_until_text_contains
from .equals import wait_until_text_equals


class WaitUntilTextDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def changes(self, xpath: str, baseline_text: str, timeout: float | None = None) -> None:
        """Wait until the text of an element changes compared to a baseline text, e.g. after a form action.

        Args:
            xpath (str): XPath of the text element.
            baseline_text (str): Baseline text to compare the new text against. It's evaluated as any change.
            timeout (float | None, optional): In seconds. Timeout to wait for text in element to change. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_changes(self._browser_driver, xpath, baseline_text, timeout)

    def contains(self, xpath: str, regex: str, timeout: float | None = None) -> None:
        """Wait until the text of an element contains a specified text fragment, e.g. after a form action.

        Args:
            xpath (str): XPath of the text element.
            regex (str): The comparison can contain both a text fragment or a regular expression. Case insensitive.
            timeout (float | None, optional): In seconds. Timeout to wait for text in element to contain the fragment. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_contains(self._browser_driver, xpath, regex, timeout)

    def equals(self, xpath: str, regex: str, timeout: float | None = None) -> None:
        """Wait until the text of an element has changed to a specific text, e.g. after a form action.

        Args:
            xpath (str): XPath of the text element.
            regex (str): Regular expression to compare the text element against. Case sensitive and is evaluated as an exact match.
            timeout (float | None, optional): In seconds. Timeout to wait for text jn element to match the condition. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_text_equals(self._browser_driver, xpath, regex, timeout)
