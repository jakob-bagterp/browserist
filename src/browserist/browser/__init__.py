__all__ = []

from typing import Union
from ..model.browser import BrowserClass, BrowserSettings, BrowserType
from ..model.browser.chrome import ChromeBrowser
from ..model.browser.firefox import FirefoxBrowser

class Browser:
    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        self.settings = settings
        
    def __new__(cls, settings: Union[BrowserSettings, None] = None) -> BrowserClass:
        if settings is None:
            return ChromeBrowser()
        
        match(settings.type):
            case BrowserType.CHROME:
                return ChromeBrowser(settings)
            case BrowserType.FIREFOX:
                return FirefoxBrowser(settings)
