from dataclasses import dataclass
from enum import Enum

class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = 1
    FIREFOX = 2

@dataclass    
class BrowserConfig:
    """Class to configure the browser driver."""
    
    type: BrowserType
    headless: bool = False
    disable_images: bool = False
