from .....constant import timeout
from .strategy import TimeoutStrategy


class TimeoutSettings:
    """Class to configure timeout settings and strategy.

    strategy: If a function times out, should the browser continue or stop? Default is stop.

    seconds: General timeout in seconds to be applied for each function (note that a function-specific timeout overrides this)."""

    __slots__ = ["strategy", "seconds", "_is_timed_out"]

    def __init__(self, strategy: TimeoutStrategy = TimeoutStrategy.STOP, seconds: float = timeout.DEFAULT) -> None:
        self.strategy: TimeoutStrategy = strategy
        self.seconds: float = seconds
        self._is_timed_out: bool = False
