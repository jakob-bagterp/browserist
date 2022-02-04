from dataclasses import dataclass
from typing import Union
from .type import BrowserType

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False
    path_to_executable: Union[str, None] = None
