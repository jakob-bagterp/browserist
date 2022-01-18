from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from typing import Union
from .. import helper

class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = auto()
    FIREFOX = auto()

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False

class BrowserObject(ABC):
    """Abstract class that contains the web driver and its browser type and configuration."""
    
    def __init__(self, settings: BrowserSettings) -> None:
        """Initiates basic properties of the browser and web driver."""

        self.settings: BrowserSettings = settings
        self.driver: object = helper.config.set_webdriver(self.settings)
        self.options: Union[ChromeOptions, FirefoxOptions]
        self.profile: FirefoxProfile

    @abstractmethod
    def disable_images(self) -> None:
        """Method to configure web driver to disable download of images for faster browsing."""
        
        raise NotImplementedError

    @abstractmethod
    def enable_headless(self) -> None:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError
