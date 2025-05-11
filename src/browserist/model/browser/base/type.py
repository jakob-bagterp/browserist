from enum import Enum, unique


@unique
class BrowserType(Enum):
    """Class to define browser type as used in [`BrowserSettings`](browser-settings.md).

    Attributes:
        BrowserType.CHROME (Enum): Chrome browser. Default browser (except on Windows).
        BrowserType.EDGE (Enum): Edge browser. Default on Windows.
        BrowserType.FIREFOX (Enum): Firefox browser.
        BrowserType.INTERNET_EXPLORER (Enum): Internet Explorer browser.
        BrowserType.SAFARI (Enum): Safari browser.


    Example:
        Use Firefox as browser type:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        How to run multiple browsers:

        ```python title="" linenums="1" hl_lines="3-5 7"
        from browserist import Browser, BrowserSettings, BrowserType

        chrome = BrowserSettings(type=BrowserType.CHROME)
        edge = BrowserSettings(type=BrowserType.EDGE)
        firefox = BrowserSettings(type=BrowserType.FIREFOX)

        for settings in [chrome, edge, firefox]:
            with Browser(settings) as browser:
                browser.open.url("https://example.com")
                browser.wait.seconds(5)
        ```
    """

    CHROME = "Chrome"
    EDGE = "Edge"
    FIREFOX = "Firefox"
    INTERNET_EXPLORER = "Internet Explorer"
    SAFARI = "Safari"
