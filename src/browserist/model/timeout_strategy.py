from dataclasses import dataclass
from enum import Enum, unique

from ..constant import timeout


@unique
class TimeoutStrategy(Enum):
    """Define timeout strategy.

    BREAK: If something times out, stop operation.

    CONTINUE: If something times out, continue operation."""

    BREAK = "break"
    CONTINUE = "continue"


@dataclass(slots=True)
class TimeoutSettings:
    strategy: TimeoutStrategy = TimeoutStrategy.BREAK
    seconds: int = timeout.DEFAULT
    _is_timed_out: bool = False
