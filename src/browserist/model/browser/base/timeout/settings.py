from dataclasses import dataclass

from .....constant import timeout
from .strategy import TimeoutStrategy


@dataclass(slots=True)
class TimeoutSettings:
    strategy: TimeoutStrategy = TimeoutStrategy.BREAK
    seconds: int = timeout.DEFAULT
    _is_timed_out: bool = False
