from dataclasses import dataclass

from .....constant import timeout
from .strategy import TimeoutStrategy


@dataclass(slots=True)
class TimeoutSettings:
    """Class to configure timeout settings and strategy.

    strategy: If a function times out, should the browser continue or stop? Default is stop.

    seconds: General timeout in seconds to be applied for each function (unless function-specific timeout is given)."""

    strategy: TimeoutStrategy = TimeoutStrategy.STOP
    seconds: int = timeout.DEFAULT
    _is_timed_out: bool = False
