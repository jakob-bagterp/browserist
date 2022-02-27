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


def ensure_path_format_encoding_as_url(path: str) -> str:
    """Relevant for Windows where a file path name should be "file://path/to/file.html" instead of "file://path\\to\\file.html" ."""

    output = path.replace("\\", "/")  # Raw replace backslash with slash.
    # Handle exception for "file:///C:/path/to/file.html" declaration in URLs.
    if re.match(r"^file:/+[A-Za-z]:", output, re.IGNORECASE):
        output = re.sub(r"^file:/+", "file:///", output, re.IGNORECASE)
    return output


def update_path_format_if_windows(path: str) -> str:
    return ensure_path_format_encoding_as_url(path) if is_windows() else path
