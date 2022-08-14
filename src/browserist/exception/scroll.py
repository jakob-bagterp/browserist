class ScrollException(Exception):
    __slots__ = ["message"]

    def __init__(self) -> None:
        self.message = "Can't scroll. Please try again."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
