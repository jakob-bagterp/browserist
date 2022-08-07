from ...constant import timeout
from ...exception.headless import MethodNotSupportedInHeadlessModeException
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .clear import input_clear
from .select import select_input_field
from .value import input_value


class InputDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def clear(self, xpath: str, timeout: float = timeout.DEFAULT) -> None:
        """Clear input form field."""

        input_clear(self._driver, xpath, timeout)

    def select(self, xpath: str) -> None:
        """Select input field, similar to clicking the mouse on a form field."""

        if self._settings.headless:
            raise MethodNotSupportedInHeadlessModeException(
                "browser.input.select", "headless mode doesn't support interactions")

        select_input_field(self._driver, xpath)

    def value(self, xpath: str, value: str, timeout: float = timeout.DEFAULT) -> None:
        """Input value into form field."""

        input_value(self._driver, xpath, value, timeout)
