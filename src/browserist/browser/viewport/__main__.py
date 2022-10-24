from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .get.__main__ import ViewportGetDriverMethods
from .set.__main__ import ViewportSetDriverMethods


class ViewportDriverMethods(DriverMethods):
    __slots__ = ["get", "set"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.get: ViewportGetDriverMethods = ViewportGetDriverMethods(browser_driver)
        self.set: ViewportSetDriverMethods = ViewportSetDriverMethods(browser_driver)
