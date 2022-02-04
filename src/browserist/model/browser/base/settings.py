from dataclasses import dataclass
from typing import Union
from .page_load_strategy import PageLoadStrategy
from .type import BrowserType

@dataclass    
class BrowserSettings:
    """Class to configure the browser driver."""
    
    type: BrowserType = BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False
    page_load_strategy: PageLoadStrategy = PageLoadStrategy.NORMAL
    path_to_executable: Union[str, None] = None
