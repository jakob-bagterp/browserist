from enum import Enum, unique


@unique
class TimeoutStrategy(Enum):
    """Define timeout strategy.

    STOP: If something times out, stop operation.

    CONTINUE: If something times out, continue operation."""

    STOP = "stop"
    CONTINUE = "continue"
