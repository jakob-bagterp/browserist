from .....constant import timeout
from .....model.browser.base.driver import BrowserDriver
from .....model.browser.base.settings import BrowserSettings
from .....model.driver_methods import DriverMethods
from .changes import wait_until_text_changes


class WaitUntilTextDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def changes(self, xpath: str, baseline_text: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the text of an element changes from a baseline text, e.g. after a form action. The text is evaluated as an exact match."""

        wait_until_text_changes(self._driver, xpath, baseline_text, timeout)
