from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .input_value import prompt_and_input_value


class PromptDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def input_value(self, xpath: str, prompt_message: str, validate_input_regex: str | None = None, timeout: float | None = None) -> None:
        """Prompt user for value through the terminal and insert this value into form field. Optional to validate input by regex."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            prompt_and_input_value(self._browser_driver, xpath, prompt_message, validate_input_regex, timeout)
