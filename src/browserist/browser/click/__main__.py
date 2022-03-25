from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .button import click_button
from .button_if_contains_text import click_button_if_contains_text


class ClickDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def button(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Click button."""

        click_button(self._driver, xpath, timeout)

    def button_if_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> None:

        click_button_if_contains_text(self._driver, xpath, regex, ignore_case, timeout)
