from .wait_for_element import wait_for_element
from ..constant import timeout
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def tool_count_number_of_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> int:
	wait_for_element(driver, xpath, timeout)
	elements = driver.find_elements_by_xpath(xpath)
	return len(elements)

class ToolsDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def count_number_of_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> int:

        return tool_count_number_of_elements(self._driver, xpath, timeout)
