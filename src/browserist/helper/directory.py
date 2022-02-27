import os
import re

from ..constant import directory
from .operating_system import is_windows


def create_if_not_exists(dir_name: str) -> None:
    if dir_name == directory.CURRENT:
        return
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def ensure_trailing_slash(dir_name: str) -> str:
    return dir_name if dir_name[-1] == "/" else f"{dir_name}/"


def replace_path_slash_with_backslash(path: str) -> str:
    """Relevant for Windows where a file path name should be "file://path\\to\\file.html" instead of "file://path/to/file.html"."""

    output = path.replace("/", "\\")  # Raw replace slash with backslash.
    # Handle exception for "file://", "file:///", etc. declaration in URLs.
    if file_prefix_backslash := re.match(r"^file:[\\]+", output, re.IGNORECASE).group(0):
        count_backslash = file_prefix_backslash.count("\\")
        file_prefix_slash = f"file:{''.join(['/' for _ in range(count_backslash)])}"
        output = output.replace(file_prefix_backslash, file_prefix_slash)
    return output


def update_path_format_if_windows(path: str) -> str:
    return replace_path_slash_with_backslash(path) if is_windows() else path
