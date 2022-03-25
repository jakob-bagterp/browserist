from ...exception.headless import MethodNotSupportedInHeadlessModeException
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .input_field import select_input_field


class SelectDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def input_field(self, xpath: str) -> None:
        """Select input field, similar to clicking the mouse on a form field."""

        if self._settings.headless:
            raise MethodNotSupportedInHeadlessModeException(
                "select.input_field", "headless mode doesn't support interactions")

        select_input_field(self._driver, xpath)
