from typing import Any

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
        """Check if input matches regex condition."""

        if self._timeout_should_continue():
            return tool_is_input_valid(text, regex, ignore_case)

    def is_url_valid(self, url: str) -> bool:  # type: ignore
        """Check if input is a valid URL."""

        if self._timeout_should_continue():
            return helper.url.is_valid(url)

    def count_elements(self, xpath: str, timeout: float | None = None) -> int:  # type: ignore
        """Count number of elements."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return tool_count_elements(self._browser_driver, xpath, timeout)

    def execute_script(self, script: str, element: object | None = None) -> Any:
        """Execute JavaScript. The element is optional."""

        if self._timeout_should_continue():
            return execute_script(self._browser_driver, script, element)
