from ...exception.headless import MethodNotSupportedInHeadlessModeException
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .input_field import select_input_field


class SelectDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def input_field(self, xpath: str, timeout: int | None = None) -> None:
        """Select input field, similar to clicking the mouse on a form field."""

        if self._browser_driver.settings.headless:
            raise MethodNotSupportedInHeadlessModeException(
                "select.input_field", "headless mode doesn't support interactions")

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            select_input_field(self._browser_driver, xpath, timeout)
