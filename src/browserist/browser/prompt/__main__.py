from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .proceed_yes_or_no import prompt_proceed_yes_or_no


class PromptDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def prompt_proceed_yes_or_no(self) -> bool:
        """Prompt user whether to proceed or not through the terminal."""

        if self._timeout_should_continue():
            return prompt_proceed_yes_or_no()
        else:
            return False
