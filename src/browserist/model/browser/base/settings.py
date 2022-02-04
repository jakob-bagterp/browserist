from dataclasses import dataclass
from .type import BrowserType

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False
