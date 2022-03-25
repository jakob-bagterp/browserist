from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .hover import mouse_hover


class MouseDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def hover(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Simulate moving the mouse cursor over the middle of an element."""

        mouse_hover(self._driver, xpath, timeout)
