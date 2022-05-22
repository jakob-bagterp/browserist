from ..model.type.callable import DriverGetBoolCallable, DriverGetTextCallable


class RetryTimeoutException(Exception):
    __slots__ = ["message"]

    def __init__(self, func: DriverGetBoolCallable | DriverGetTextCallable) -> None:
        self.message = f"Retry function timed out as loop ran out of retries for this function: {func}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
