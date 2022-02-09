import re
from .wait_for_element import wait_for_element
from ..constant import regex, timeout
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def is_url_valid(url: str) -> bool:
    return bool(re.match(regex.VALID_URL, url, re.IGNORECASE))

def tool_count_number_of_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> int:
	wait_for_element(driver, xpath, timeout)
	elements = driver.find_elements_by_xpath(xpath)
	return len(elements)

class ToolsDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        
    def is_url_valid(self, url: str) -> bool:
        """Check if input is a valid URL."""

        return is_url_valid(url)

    def count_number_of_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> int:
        """Count number of elements."""

        return tool_count_number_of_elements(self._driver, xpath, timeout)
