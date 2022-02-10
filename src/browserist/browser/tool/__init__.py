from .count_number_of_elements import tool_count_number_of_elements
from .is_input_valid import tool_is_input_valid
from .is_url_valid import tool_is_url_valid
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class ToolDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def is_input_valid(self, text: str, regex: str, ignore_case: bool = True) -> bool:
        """Check if input matches regex condition."""

        return tool_is_input_valid(text, regex, ignore_case)

    def is_url_valid(self, url: str) -> bool:
        """Check if input is a valid URL."""

        return tool_is_url_valid(url)

    def count_number_of_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> int:
        """Count number of elements."""

        return tool_count_number_of_elements(self._driver, xpath, timeout)
