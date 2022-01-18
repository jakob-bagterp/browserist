from abc import ABC, abstractmethod
from dataclasses import dataclass, InitVar
from enum import Enum, unique
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from .. import helper

@unique
class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = "Chrome"
    FIREFOX = "Firefox"

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False

@dataclass
class BrowserClass(ABC):
    """Abstract class that contains the web driver based on browser type and configuration."""

    settings: BrowserSettings = BrowserSettings()
    initvar_settings: InitVar[BrowserSettings]
    chrome_options: ChromeOptions = ChromeOptions()
    firefox_options: FirefoxOptions = FirefoxOptions()
    firefox_profile: FirefoxProfile = FirefoxProfile()
    
    def __post_init__(self, settings: BrowserSettings) -> None:
        """Initiates basic properties of the browser and web driver."""

        self.settings = settings

    @abstractmethod
    def disable_images(self) -> None:
        """Method to configure web driver to disable download of images for faster browsing."""
        
        raise NotImplementedError

    @abstractmethod
    def enable_headless(self) -> None:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError
