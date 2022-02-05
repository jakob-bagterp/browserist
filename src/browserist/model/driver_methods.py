from .browser.base.driver import BrowserDriver

class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    def __init__(self, browser_driver: BrowserDriver) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._driver: object = browser_driver.webdriver
