class FilePNGSyntaxError(Exception):
    __slots__ = ["message"]

    def __init__(self, file_name: str) -> None:
        self.message = f"Invalid PNG file name: {file_name}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
