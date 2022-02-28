from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .clear import input_clear
from .value import input_value


class InputDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def clear(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Clear input form field."""

        input_clear(self._driver, xpath, timeout)

    def value(self, xpath: str, value: str, timeout: int = timeout.DEFAULT) -> None:
        """Input value into form field."""

        input_value(self._driver, xpath, value, timeout)
