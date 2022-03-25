from .browser.base.driver import BrowserDriver
from .browser.base.settings import BrowserSettings


class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._driver: object = browser_driver.webdriver
        self._settings: BrowserSettings = settings
