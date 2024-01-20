from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .input_value import prompt_and_input_value
from .proceed_yes_or_no import prompt_proceed_yes_or_no


class PromptDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def input_value(self, xpath: str, prompt_message: str, validate_input_regex: str | None = None, timeout: float | None = None) -> None:
        """Prompt user for value through the terminal and insert this value into form field.

        Args:
            xpath (str): XPath of form field to insert value into.
            prompt_message (str): Message to prompt user with in the terminal.
            validate_input_regex (str | None, optional): If provided, the input value will be validated against this regex.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            prompt_and_input_value(self._browser_driver, xpath, prompt_message, validate_input_regex, timeout)

    def proceed_yes_or_no(self) -> bool:
        """Prompt user in the terminal whether to proceed or not.

        Returns:
            bool: `True` if user wants to proceed, `False` otherwise.
        """

        if self._timeout_should_continue():
            return prompt_proceed_yes_or_no()
        else:
            return False
