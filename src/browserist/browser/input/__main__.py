from ...exception.headless import MethodNotSupportedInHeadlessModeException
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .clear import clear_input_field
from .select import select_input_field
from .value import input_value


class InputDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def clear(self, xpath: str, timeout: float | None = None) -> None:
        """Clear any text input from form field.

        Args:
            xpath (str): XPath of the input field.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            clear_input_field(self._browser_driver, xpath, timeout)

    def select(self, xpath: str, timeout: float | None = None) -> None:
        """Select input field, similar to clicking the mouse on a form field.

        Args:
            xpath (str): XPath of the input field.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Raises:
            MethodNotSupportedInHeadlessModeException: Raised if the browser is in headless mode.
        """

        if self._browser_driver.settings.headless:
            self._set_is_timed_out()
            if not self._timeout_should_continue():
                raise MethodNotSupportedInHeadlessModeException(
                    "browser.input.select", "headless mode doesn't support interactions")

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            select_input_field(self._browser_driver, xpath, timeout)

    def value(self, xpath: str, value: str, timeout: float | None = None) -> None:
        """Input value into form field.

        Args:
            xpath (str): XPath of the element.
            value (str): Input value.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            input_value(self._browser_driver, xpath, value, timeout)
