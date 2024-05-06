class ScrollException(Exception):
    __slots__ = ["message"]

    def __init__(self) -> None:
        self.message = "Can't scroll. Please try again."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class PageValueError(Exception):
    __slots__ = ["message"]

    def __init__(self, pages: int) -> None:
        self.message = f"Invalid page value. Must be an integer of 1 or greater, not this: {pages}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
