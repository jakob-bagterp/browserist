from enum import Enum, unique

@unique
class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""
    
    CHROME = "Chrome"
    EDGE = "Edge"
    INTERNET_EXPLORER = "Internet Explorer"
    FIREFOX = "Firefox"
    OPERA = "Opera"
    SAFARI = "Safari"
