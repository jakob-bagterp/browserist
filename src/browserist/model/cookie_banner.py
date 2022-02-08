from dataclasses import dataclass
from typing import Union
from ..constant import timeout

@dataclass
class CookieBannerSettings:
    """Object with data needed to accept or decline cookies from a banner.
    
    button_xpath: Can be for either accept of decline cookies.
    
    url: Optional URL from where to handle the cookie banner.
    
    has_loaded_wait_seconds: Minor grace time to make sure the cookie banner has loaded.
    
    has_loaded_xpath: Check if banner element has loaded so the cookie banner is ready.
    
    has_disappeared_wait_seconds: Minor grace time to make sure the cookie banner has disappeared and that the cookie information has been saved before proceeding."""

    button_xpath: str
    url: Union[str, None] = None
    has_loaded_wait_seconds: int = timeout.DEFAULT
    has_loaded_xpath: Union[str, None] = None
    has_disappeared_wait_seconds: int = timeout.SHORT
