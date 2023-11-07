from typing import Any

from selenium.webdriver.remote.webelement import WebElement

from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .count_elements import tool_count_elements
from .execute_script import execute_script
from .is_input_valid import tool_is_input_valid


class ToolDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def is_input_valid(self, text: str, regex: str, ignore_case: bool = True) -> bool:  # type: ignore
        """Check if text input matches regex condition.

        Args:
            text (str): Input text.
            regex (str): Condition as regular expression.
            ignore_case (bool, optional): Ignore case when comparing input text to condition.

        Returns:
            bool: `True` if input matches condition, `False` otherwise.
        """

        if self._timeout_should_continue():
            return tool_is_input_valid(text, regex, ignore_case)

    def is_url_valid(self, url: str) -> bool:  # type: ignore
        """Check if input is a valid URL.

        Args:
            url (str): Input URL.

        Returns:
            bool: `True` if input is a valid URL, `False` otherwise.
        """

        if self._timeout_should_continue():
            return helper.url.is_valid(url)

    def is_xpath_valid(self, xpath: str) -> bool:  # type: ignore
        """Check if input is a valid XPath expression.

        Args:
            xpath (str): Input XPath.

        Returns:
            bool: `True` if input is a valid XPath expression, `False` otherwise.
        """

        if self._timeout_should_continue():
            return helper.xpath.is_valid(xpath)

    def count_elements(self, xpath: str, timeout: float | None = None) -> int:  # type: ignore
        """Count number of elements.

        Args:
            xpath (str): XPath of the elements.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            int: Number of elements.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return tool_count_elements(self._browser_driver, xpath, timeout)

    def execute_script(self, script: str, element: WebElement | None = None) -> Any:
        """Execute JavaScript, either with WebElement or without.

        Args:
            script (str): JavaScript code.
            element (WebElement | None, optional): If given, execute JavaScript with WebElement.

        Returns:
            Any: Return value given by the JavaScript code.
        """

        if self._timeout_should_continue():
            return execute_script(self._browser_driver, script, element)
