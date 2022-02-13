from .iframe import switch_to_iframe
from .original_page import switch_to_original_page
from .window import switch_to_window
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class SwitchToDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings, original_window_handle: str) -> None:
        super().__init__(browser_driver, settings)
        self._original_window_handle = original_window_handle

    def iframe(self, xpath: str) -> None:
        """Switch to iframe."""

        switch_to_iframe(self._driver, xpath)

    def original_page(self) -> None:
        """After switch to iframe, use this to go back to the original page."""

        switch_to_original_page(self._driver)

    def original_window(self) -> None:
        """Switch to initial window."""

        switch_to_window(self._driver, self._original_window_handle)

    def window(self, window_handle: str) -> None:
        """Switch to window by handle ID."""

        switch_to_window(self._driver, window_handle)
