from enum import Enum, unique


@unique
class TimeoutStrategy(Enum):
    """Define timeout strategy as used in [`TimeoutSettings`](timeout-settings.md).

    Attributes:
        TimeoutStrategy.STOP (Enum): If a function times out, stop operation.
        TimeoutStrategy.CONTINUE (Enum): If a function times out, continue operation.

    Example:
        How to set a different timeout strategy than the default `STOP`:

        ```python title="" linenums="1" hl_lines="3-4"
        from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

        timeout_settings = TimeoutSettings(
            strategy=TimeoutStrategy.CONTINUE)

        settings = BrowserSettings(timeout=timeout_settings)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    STOP = "stop"
    CONTINUE = "continue"


class TimeoutSettings:
    """Class to configure timeout settings and strategy as used in [`BrowserSettings`](browser-settings.md).

    Args:
        strategy (TimeoutStrategy, optional): If a function times out, should the browser continue or stop? Default is stop.
        seconds (float, optional): General timeout in seconds to be applied for each function (note that a function-specific timeout overrides this).
        idle_download_seconds (float, optional): General timeout in seconds to be applied for downloads to determine when a file download is idle.

    Example:
        How to set the timeout strategy and timeout:

        ```python title="" linenums="1" hl_lines="3-5"
        from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

        timeout_settings = TimeoutSettings(
            strategy=TimeoutStrategy.CONTINUE,
            seconds=10)

        settings = BrowserSettings(timeout=timeout_settings)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    __slots__ = ["strategy", "seconds", "idle_download_seconds", "_is_timed_out"]

    def __init__(
        self, strategy: TimeoutStrategy = TimeoutStrategy.STOP, seconds: float = 5, idle_download_seconds: float = 3
    ) -> None:
        self.strategy: TimeoutStrategy = strategy
        self.seconds: float = seconds
        self.idle_download_seconds: float = idle_download_seconds
        self._is_timed_out: bool = False
