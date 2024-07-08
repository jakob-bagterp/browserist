from enum import Enum, unique


@unique
class BrowserType(Enum):
    """Class to define browser type.

    Attributes:
        CHROME: Chrome browser.
        EDGE: Edge browser.
        FIREFOX: Firefox browser.
        INTERNET_EXPLORER: Internet Explorer browser.
        SAFARI: Safari browser.
    """

    CHROME = "Chrome"
    EDGE = "Edge"
    FIREFOX = "Firefox"
    INTERNET_EXPLORER = "Internet Explorer"
    SAFARI = "Safari"
