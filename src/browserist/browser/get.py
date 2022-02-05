from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

class Get(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current_url(self) -> str:
        return self._driver.current_url
