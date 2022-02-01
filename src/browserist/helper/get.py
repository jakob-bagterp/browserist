from typing import Union
from ..model.browser._driver import BrowserDriver
from ..model.browser._settings import BrowserSettings
from ..model.browser._type import BrowserType
from ..model.browser.chrome import ChromeBrowserDriver
from ..model.browser.firefox import FirefoxBrowserDriver

def browser_driver(settings: Union[BrowserSettings, None] = None) -> BrowserDriver:
    if settings is None:
        return ChromeBrowserDriver()
    
    match(settings.type):
        case BrowserType.CHROME:
            return ChromeBrowserDriver(settings)
        case BrowserType.FIREFOX:
            return FirefoxBrowserDriver(settings)
        case _:
            raise ValueError(settings.type)
