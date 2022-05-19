from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .element_disappears import wait_until_element_disappears
from .number_of_window_handles_is import wait_until_number_of_window_handles_is


class WaitUntilDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def element_disappears(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist."""

        wait_until_element_disappears(self._driver, xpath, timeout)

    def until_number_of_window_handles_is(self, timeout: int = timeout.DEFAULT) -> None:
        """Wait until number of window handles is."""

        wait_until_number_of_window_handles_is(self._driver, timeout)
