from .clear import input_clear
from .value import input_value
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

class InputDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
    
    def clear(self, input_xpath: str) -> None:
        """Clear input form field."""

        input_clear(self._driver, input_xpath)

    def value(self, input_xpath: str, value: str) -> None:
        """Input value into form field."""

        input_value(self._driver, input_xpath, value)
