from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.chrome import ChromeBrowserDriver
from ..model.browser.edge import EdgeBrowserDriver
from ..model.browser.firefox import FirefoxBrowserDriver
from ..model.browser.internet_explorer import InternetExplorerBrowserDriver
from ..model.browser.opera import OperaBrowserDriver
from ..model.browser.safari import SafariBrowserDriver


def browser_driver(settings: BrowserSettings) -> BrowserDriver:
    match(settings.type):
        case BrowserType.CHROME:
            return ChromeBrowserDriver(settings)
        case BrowserType.EDGE:
            return EdgeBrowserDriver(settings)
        case BrowserType.FIREFOX:
            return FirefoxBrowserDriver(settings)
        case BrowserType.INTERNET_EXPLORER:
            return InternetExplorerBrowserDriver(settings)
        case BrowserType.OPERA:
            return OperaBrowserDriver(settings)
        case BrowserType.SAFARI:
            return SafariBrowserDriver(settings)
        case _:
            raise ValueError(settings.type)
