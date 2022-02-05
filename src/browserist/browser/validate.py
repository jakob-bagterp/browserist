from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

class ValidateDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
