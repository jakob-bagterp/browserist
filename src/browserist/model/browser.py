from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any
from .. import helper

class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = 1
    FIREFOX = 2

@dataclass    
class BrowserConfig:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False

class BrowserObject(ABC):
    """Abstract class that contains the web driver and its browser type and configuration."""
    
    def __init__(self, config: BrowserConfig) -> None:
        """Initiates basic properties of the browser and web driver."""

        self.config: BrowserConfig = config
        self.driver: object = helper.config.set_webdriver(self.config)

    @abstractmethod
    def disable_images(*args, **kwargs) -> Any:
        """Method to configure web driver to disable download of images for faster browsing."""
        
        raise NotImplementedError

    @abstractmethod
    def enable_headless(*args, **kwargs) -> Any:
        """Method to enable headless version of web driver (i.e. don't open browser window) for faster browsing."""

        raise NotImplementedError
