from abc import ABC, abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.remote.webdriver import BaseWebDriver, WebDriver
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.safari.service import Service as SafariService

from .... import helper
from .settings import BrowserSettings
from .type import BrowserType


class BrowserDriver(ABC):
    """Abstract class that contains the Selenium web driver based on browser type and configuration."""

    __slots__ = ["settings", "chrome_options", "chrome_service", "edge_options", "edge_service", "firefox_options", "firefox_service", "ie_options", "ie_service", "safari_options", "safari_service", "webdriver"]

    def __init__(self, settings: BrowserSettings) -> None:
        """Initiates basic properties of the Selenium web driver."""

        self.settings = settings
        if self.settings.check_connection and not helper.internet.has_connection():
            raise ConnectionError("No internet connection.")
        helper.directory.create_if_not_exists(self.settings._download_dir)
        helper.directory.create_if_not_exists(self.settings._screenshot_dir)

        match(self.settings.type):
            case BrowserType.CHROME:
                self.chrome_options: ChromeOptions = ChromeOptions()
                self.chrome_service: ChromeService = self.set_service()  # type: ignore
            case BrowserType.EDGE:
                self.edge_options: EdgeOptions = EdgeOptions()
                self.edge_service: EdgeService = self.set_service()  # type: ignore
            case BrowserType.FIREFOX:
                self.firefox_options: FirefoxOptions = FirefoxOptions()
                self.firefox_service: FirefoxService = self.set_service()  # type: ignore
            case BrowserType.INTERNET_EXPLORER:
                self.ie_options: IEOptions = IEOptions()
                self.ie_service: IEService = self.set_service()  # type: ignore
            case BrowserType.SAFARI:
                self.safari_options: SafariOptions = SafariOptions()
                self.safari_service: SafariService = self.set_service()  # type: ignore

        self.ensure_browser_type()
        self.set_options_and_profile()
        self.webdriver: BaseWebDriver = self.set_webdriver()

    @abstractmethod
    def ensure_browser_type(self) -> None:
        """Method to ensure the correct browser type if a specific browser instance is created directly from a subclass (e.g. FirefoxBrowserDriver) without the optional settings as argument, simply as Chrome is default browser."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_webdriver(self) -> BaseWebDriver:
        """Method to set web driver based on the settings."""

        raise NotImplementedError  # pragma: no cover

    def set_options_and_profile(self) -> None:
        """Internal task initializer that runs the configuration methods to disable images, enable headless, etc."""

        self.disable_images()
        self.enable_headless()
        self.set_download_directory()
        self.set_page_load_strategy()
        self.disable_default_search_engine_prompt()
        self.set_user_agent()
        self.set_proxy()

    @abstractmethod
    def disable_images(self) -> None:
        """Method to configure web driver to disable download of images for faster browsing."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def enable_headless(self) -> None:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_download_directory(self) -> None:
        """Method to set the default download directory."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_page_load_strategy(self) -> None:
        """Method to set the page load strategy to define whether the web driver should wait until all assets are downloaded (slower) or not (faster)."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def disable_default_search_engine_prompt(self) -> None:
        """Method to disable the default search engine prompt."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_user_agent(self) -> None:
        """Method to set the user agent."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_proxy(self) -> None:
        """Method to set the proxy."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def set_service(self) -> Service:
        """Method to set the service."""

        raise NotImplementedError  # pragma: no cover

    def get_webdriver(self) -> WebDriver:
        """Returns the Selenium web driver."""

        return self.webdriver  # type: ignore
