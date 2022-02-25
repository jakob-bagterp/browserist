from enum import Enum, unique


@unique
class PageLoadStrategy(Enum):
    """Class to configure page load strategy for Selenium.

    NORMAL: Used by default. Waits for all resources to download. Ready state: Complete.

    EAGER: DOM access is ready, but other resources like images may still be loading. Ready state: Interactive.

    NONE: Does not block web driver at all. Ready state: Any."""

    NORMAL = "normal"
    EAGER = "eager"
    NONE = "none"
