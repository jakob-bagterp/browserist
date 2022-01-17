from abc import ABC
from dataclasses import dataclass
from enum import Enum
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
