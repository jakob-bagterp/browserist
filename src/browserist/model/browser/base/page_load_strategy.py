from enum import Enum, unique


@unique
class PageLoadStrategy(Enum):
    """Class to configure page load strategy for Selenium as used in [`BrowserSettings`](browser-settings.md).

    Attributes:
        PageLoadStrategy.NORMAL (Enum): Used by default. Waits for all resources to download. Ready state: Complete.
        PageLoadStrategy.EAGER (Enum): DOM access is ready, but other resources like images may still be loading. Ready state: Interactive.
        PageLoadStrategy.NONE (Enum): Does not block web driver at all. Ready state: Any.

    Example:
        How to change the default page load strategy to eager:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings, PageLoadStrategy

        settings = BrowserSettings(page_load_strategy=PageLoadStrategy.EAGER)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    NORMAL = "normal"
    EAGER = "eager"
    NONE = "none"
