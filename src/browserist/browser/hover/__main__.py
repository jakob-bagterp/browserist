from .mouse_to_element import hover_mouse_on_element
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class HoverDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def mouse_on_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Simulate moving the mouse cursor over the middle of an element."""

        hover_mouse_on_element(self._driver, xpath, timeout)
