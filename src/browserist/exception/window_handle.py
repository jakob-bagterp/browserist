class WindowHandleIdNotFoundError(Exception):
    __slots__ = ["message"]

    def __init__(self, id: str) -> None:
        self.message = f"Window handle ID not found or doesn't exist: {id}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleNameNotFoundError(Exception):
    __slots__ = ["message"]

    def __init__(self, name: str) -> None:
        self.message = f"Window handle name not found or doesn't exist: {name}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleIdNotUniqueError(Exception):
    __slots__ = ["message"]

    def __init__(self, id: str) -> None:
        self.message = f"Window handle ID already exists: {id}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleNameNotUniqueError(Exception):
    __slots__ = ["message"]

    def __init__(self, name: str) -> None:
        self.message = f"Window handle name already exists: {name}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleIdNotValidError(Exception):
    __slots__ = ["message"]

    def __init__(self, id: str) -> None:
        self.message = f"Window handle ID has invalid format: {id}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleNameNotValidError(Exception):
    __slots__ = ["message"]

    def __init__(self, name: str) -> None:
        self.message = f"Window handle name is invalid. Try using another name than this: {name}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
