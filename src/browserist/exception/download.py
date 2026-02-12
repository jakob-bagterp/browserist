class DownloadHandlerMultipleFinalFilesError(Exception):
    __slots__ = ["message"]

    def __init__(self, files: list[str]) -> None:
        self.message = (
            f"Multiple final files found. Not possible to determine which is for this download: {', '.join(files)}"
        )
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class DownloadHandlerMultipleTemporaryFilesError(Exception):
    __slots__ = ["message"]

    def __init__(self, files: list[str]) -> None:
        self.message = (
            f"Multiple temporary files found. Not possible to determine which is for this download: {', '.join(files)}"
        )
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
