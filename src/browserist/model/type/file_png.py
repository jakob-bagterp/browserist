from __future__ import annotations

from ...exception.file_png import FilePNGSyntaxError


class FilePNG(str):
    """Class to handle and validate PNG image files as "tiny type"."""

    __slots__ = ["value"]

    def __new__(cls, file_name: str | FilePNG) -> FilePNG:
        # If input already is a validated PNG image file, bypass and don't create a new object:
        return file_name if isinstance(file_name, FilePNG) else super().__new__(cls, file_name)

    def __init__(self, file_name: str) -> None:
        self.value: str = file_name
        if not self.is_valid():
            raise FilePNGSyntaxError(file_name)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def is_valid(self) -> bool:
        return bool(self.value.endswith(".png"))
