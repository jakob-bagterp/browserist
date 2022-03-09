class WindowHandleNameNotUniqueError(Exception):
    def __init__(self, name: str) -> None:
        self.message = f"Window handle name already exists: {name}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WindowHandleIdNotValidError(Exception):
    def __init__(self, id: str) -> None:
        self.message = f"Window handle ID has invalid format: {id}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
