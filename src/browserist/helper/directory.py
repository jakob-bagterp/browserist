import os
import re
import urllib

from ..constant import directory
from . import operating_system


def create_if_not_exists(dir_name: str) -> None:
    if dir_name == directory.CURRENT:
        return
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def ensure_trailing_slash(dir_name: str) -> str:
    return dir_name if dir_name[-1] == "/" else f"{dir_name}/"


def encode_path_as_url(path: str) -> str:
    return urllib.parse.quote(path, safe="/:").replace("%2520", "%20")


def ensure_windows_file_path_format_encoding_as_url(path: str) -> str:
    """Relevant for Windows where a file path name should be "file://path/to/file.html" instead of "file://path\\to\\file.html" ."""

    output = path.replace("\\", "/")  # Raw replace backslash with slash.
    # Handle exception for "file:///C:/path/to/file.html" declaration in URLs.
    if re.match(r"^file:/+[A-Za-z]:", output, re.IGNORECASE):
        output = re.sub(r"^file:/+", "file:///", output, re.IGNORECASE)
    return encode_path_as_url(output)


def update_path_format_if_windows(path: str) -> str:
    return ensure_windows_file_path_format_encoding_as_url(path) if operating_system.is_windows() else encode_path_as_url(path)
