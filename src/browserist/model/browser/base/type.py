from enum import Enum, unique


@unique
class BrowserType(Enum):
    """Class to define browser type, e.g. Chrome, Firefox, etc."""

    CHROME = "Chrome"
    EDGE = "Edge"
    FIREFOX = "Firefox"
    INTERNET_EXPLORER = "Internet Explorer"
    OPERA = "Opera"
    SAFARI = "Safari"
