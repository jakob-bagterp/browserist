from dataclasses import dataclass
from enum import Enum, auto

from ..constant import timeout


class TimeoutStrategy(Enum):
    """Define timeout strategy.

    BREAK: If something times out, stop operation.

    CONTINUE: If something times out, continue operation."""

    BREAK = auto()
    CONTINUE = auto()


@dataclass
class TimeoutSettings:
    strategy: TimeoutStrategy = TimeoutStrategy.BREAK
    seconds: int = timeout.DEFAULT
    _is_timed_out: bool = False
