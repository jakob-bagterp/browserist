from __future__ import annotations

from pathlib import Path


class FilePath(str):
    """Class to handle directory or file paths as "tiny type". It converts and stores the value as a Path object. Intended for internal use only and to handle both string and Path inputs."""

    __slots__ = ["path"]

    def __new__(cls, path: str | Path) -> FilePath:
        # If input already is a validated path, bypass and don't create a new object:
        return path if isinstance(path, FilePath) else super().__new__(cls, path)

    def __init__(self, path: str | Path) -> None:
        self.path: Path = path if isinstance(path, Path) else Path(path)

    def __str__(self) -> str:
        return str(self.path.resolve())

    def __repr__(self) -> str:
        return str(self.path.resolve())

    @property
    def name(self) -> str:
        """Return the name of the file or directory. For example: `file.zip` from `/path/to/file.zip`."""

        return self.path.name
