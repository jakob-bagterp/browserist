from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .button import click_button
from .button_if_contains_text import click_button_if_contains_text


class ClickDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def button(self, xpath: str, timeout: float | None = None) -> None:
        """Click button."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button(self._browser_driver, xpath, timeout)

    def button_if_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: float | None = None) -> None:
        """Click button if contains certain text or a regular expression."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button_if_contains_text(self._browser_driver, xpath, regex, ignore_case, timeout)
