from dataclasses import dataclass

from .....constant import timeout
from .strategy import TimeoutStrategy


@dataclass(kw_only=True, slots=True)
class TimeoutSettings:
    """Class to configure timeout settings and strategy.

    strategy: If a function times out, should the browser continue or stop? Default is stop.

    seconds: General timeout in seconds to be applied for each function (note that a function-specific timeout overrides this)."""

    strategy: TimeoutStrategy = TimeoutStrategy.STOP
    seconds: int = timeout.DEFAULT
    _is_timed_out: bool = False
