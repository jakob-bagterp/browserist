import os
import re

from ..constant import directory


def create_if_not_exists(dir_name: str) -> None:
    if dir_name == directory.CURRENT:
        return
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def ensure_trailing_slash(dir_name: str) -> str:
    return dir_name if dir_name[-1] == "/" else f"{dir_name}/"


def replace_path_slash_with_backslash(path: str) -> str:
    """Relevant for Windows where a file path name should be "file://path\\to\\file.html" instead of "file://path/to/file.html"."""

    path = path.replace("/", "\\")  # Raw replace slash with backslash.
    return re.sub(r"^file:[\\]+", "file://", path)  # Handle exceptions for "file://" declaration in URLs.
