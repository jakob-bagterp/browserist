from enum import Enum, unique

from ....constant import idle_timeout, timeout


@unique
class TimeoutStrategy(Enum):
    """Define timeout strategy.

    Attributes:
        STOP: If a function times out, stop operation.
        CONTINUE: If a function times out, continue operation.
    """

    STOP = "stop"
    CONTINUE = "continue"


class TimeoutSettings:
    """Class to configure timeout settings and strategy.

    Args:
        strategy (TimeoutStrategy, optional): If a function times out, should the browser continue or stop? Default is stop.
        seconds (float, optional): General timeout in seconds to be applied for each function (note that a function-specific timeout overrides this).
        idle_download_seconds (float, optional): General timeout in seconds to be applied for downloads to determine when a file download is idle.
    """

    __slots__ = ["strategy", "seconds", "idle_download_seconds", "_is_timed_out"]

    def __init__(self, strategy: TimeoutStrategy = TimeoutStrategy.STOP, seconds: float = timeout.DEFAULT, idle_download_seconds: float = idle_timeout.DEFAULT) -> None:
        self.strategy: TimeoutStrategy = strategy
        self.seconds: float = seconds
        self.idle_download_seconds: float = idle_download_seconds
        self._is_timed_out: bool = False
