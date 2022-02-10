from .is_input_valid import tools_is_input_valid
from .is_url_valid import tools_is_url_valid
from ..wait.for_element import wait_for_element
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

def tool_count_number_of_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> int:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return len(elements)

class ToolsDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def is_input_valid(self, text: str, regex: str, ignore_case: bool = True) -> bool:
        """Check if input matches regex condition."""

        return tools_is_input_valid(text, regex, ignore_case)

    def is_url_valid(self, url: str) -> bool:
        """Check if input is a valid URL."""

        return tools_is_url_valid(url)

    def count_number_of_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> int:
        """Count number of elements."""

        return tool_count_number_of_elements(self._driver, xpath, timeout)
