from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def get_current_url(driver: object) -> str:
    return driver.current_url

class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current_url(self) -> str:
        """Get URL of the current page."""
        
        return get_current_url(self._driver)
