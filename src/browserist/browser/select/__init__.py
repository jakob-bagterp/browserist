from .wait_for_element import wait_for_element
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def select_input_field(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    driver.find_element_by_xpath(xpath).click()

class SelectDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def input_field(self, xpath: str) -> None:
        """Select input field, similar to clicking the mouse on a form field."""

        select_input_field(self._driver, xpath)
