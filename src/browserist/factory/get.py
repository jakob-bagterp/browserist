from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.chrome import ChromeBrowserDriver
from ..model.browser.edge import EdgeBrowserDriver
from ..model.browser.firefox import FirefoxBrowserDriver
from ..model.browser.internet_explorer import InternetExplorerBrowserDriver
from ..model.browser.safari import SafariBrowserDriver
from ..model.download.chrome import ChromeDownloadHandler
from ..model.download.edge import EdgeDownloadHandler
from ..model.download.firefox import FirefoxDownloadHandler
from ..model.download.handler import DownloadHandler
from ..model.download.internet_explorer import InternetExplorerDownloadHandler
from ..model.download.safari import SafariDownloadHandler


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


def download_handler(browser_driver: BrowserDriver, download_dir_entries_before_download: list[str], idle_download_timeout: float) -> DownloadHandler:
    match(browser_driver.settings.type):
        case BrowserType.CHROME:
            return ChromeDownloadHandler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        case BrowserType.EDGE:
            return EdgeDownloadHandler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        case BrowserType.FIREFOX:
            return FirefoxDownloadHandler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        case BrowserType.INTERNET_EXPLORER:
            return InternetExplorerDownloadHandler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        case BrowserType.SAFARI:
            return SafariDownloadHandler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        case _:
            raise ValueError(browser_driver.settings.type)
