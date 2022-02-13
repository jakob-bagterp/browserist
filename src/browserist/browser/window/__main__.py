from .get.__main__ import WindowGetDriverMethods
from .set.__main__ import WindowSetDriverMethods
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class WindowDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.get: WindowGetDriverMethods = WindowGetDriverMethods(browser_driver, settings)
        self.set: WindowSetDriverMethods = WindowSetDriverMethods(browser_driver, settings)
