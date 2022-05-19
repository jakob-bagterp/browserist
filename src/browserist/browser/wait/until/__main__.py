from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .element_disappears import wait_until_element_disappears


class WaitUntilDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def element_disappears(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist."""

        wait_until_element_disappears(self._driver, xpath, timeout)
