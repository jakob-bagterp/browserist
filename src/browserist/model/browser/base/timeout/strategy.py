from enum import Enum, unique


@unique
class TimeoutStrategy(Enum):
    """Define timeout strategy.

    Attributes:
        STOP: If a function times out, stop operation.
        CONTINUE: If a function times out, continue operation.
    """

    STOP = "stop"
    CONTINUE = "continue"
