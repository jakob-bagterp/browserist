from abc import ABC, abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from .... import helper
from .settings import BrowserSettings
from .type import BrowserType


class BrowserDriver(ABC):
    """Abstract class that contains the Selenium web driver based on browser type and configuration."""

    def __init__(self, settings: BrowserSettings) -> None:
        """Initiates basic properties of the Selenium web driver."""

        self.settings = settings
        helper.directory.create_if_not_exists(self.settings.screenshot_dir)

        match(self.settings.type):
            case BrowserType.CHROME | BrowserType.OPERA:
                self.chrome_options: ChromeOptions = ChromeOptions()
            case BrowserType.EDGE:
                self.edge_options: EdgeOptions = EdgeOptions()  # type: ignore
            case BrowserType.FIREFOX:
                self.firefox_options: FirefoxOptions = FirefoxOptions()  # type: ignore
                self.firefox_profile: FirefoxProfile = FirefoxProfile()  # type: ignore
            case BrowserType.INTERNET_EXPLORER:
                self.ie_options: IEOptions = IEOptions()  # type: ignore
            case BrowserType.SAFARI:
                self.safari_options: SafariOptions = SafariOptions()  # type: ignore

        self.ensure_browser_type()
        self.set_options_and_profile()
        self.webdriver: object = self.set_webdriver()

    @abstractmethod
    def ensure_browser_type(self) -> None:
        """Method to ensure the correct browser type if a specific browser instance is created directly from a subclass (e.g. FirefoxBrowserDriver) without the optional settings as argument, simply as Chrome is default browser."""

        raise NotImplementedError

    @abstractmethod
    def set_webdriver(self) -> object:
        """Method to set web driver based on the settings."""

        raise NotImplementedError

    def set_options_and_profile(self) -> None:
        """Internal task initialiser that runs the configuration methods to disable images, enable headless, etc."""

        self.disable_images()
        self.enable_headless()
        self.set_page_load_strategy()

    @abstractmethod
    def disable_images(self) -> None:
        """Method to configure web driver to disable download of images for faster browsing."""

        raise NotImplementedError

    @abstractmethod
    def enable_headless(self) -> None:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError

    @abstractmethod
    def set_page_load_strategy(self) -> None:
        """Method to set the page load strategy to define whether the web driver should wait until all assets are downloaded (slower) or not (faster)."""

        raise NotImplementedError
