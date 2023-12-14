from ..model.browser.base.download.handler import DownloadHandler
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.chrome import ChromeBrowserDriver, ChromeDownloadHandler
from ..model.browser.edge import EdgeBrowserDriver, EdgeDownloadHandler
from ..model.browser.firefox import FirefoxBrowserDriver, FirefoxDownloadHandler
from ..model.browser.internet_explorer import InternetExplorerBrowserDriver, InternetExplorerDownloadHandler
from ..model.browser.safari import SafariBrowserDriver, SafariDownloadHandler


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
        case BrowserType.SAFARI:
            return SafariBrowserDriver(settings)
        case _:
            raise ValueError(settings.type)


def download_handler(browser_driver: BrowserDriver) -> DownloadHandler:
    match(browser_driver.settings.type):
        case BrowserType.CHROME:
            return ChromeDownloadHandler()
        case BrowserType.EDGE:
            return EdgeDownloadHandler()
        case BrowserType.FIREFOX:
            return FirefoxDownloadHandler()
        case BrowserType.INTERNET_EXPLORER:
            return InternetExplorerDownloadHandler()
        case BrowserType.SAFARI:
            return SafariDownloadHandler()
        case _:
            raise ValueError(browser_driver.settings.type)
