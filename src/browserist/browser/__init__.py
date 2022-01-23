__all__ = []

from typing import Union
from ..model.browser import BrowserDriver, BrowserSettings, BrowserType
from ..model.browser.chrome import ChromeBrowserDriver
from ..model.browser.firefox import FirefoxBrowserDriver

class Browser:
    def __new__(cls, settings: Union[BrowserSettings, None] = None) -> BrowserDriver:
        if settings is None:
            return ChromeBrowserDriver()
        
        match(settings.type):
            case BrowserType.CHROME:
                return ChromeBrowserDriver(settings)
            case BrowserType.FIREFOX:
                return FirefoxBrowserDriver(settings)
            case _:
                raise ValueError(settings.type)

    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        self.settings = settings
