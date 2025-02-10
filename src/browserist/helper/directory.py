import os
import re
import urllib

from ..constant import directory
from ..model.type.path import FilePath
from . import operating_system


def create_if_not_exists(dir_name: FilePath) -> None:
    if dir_name.path == directory.PROJECT_WORKING_DIR:
        return
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def encode_path_as_url(path: str) -> str:
    url_encoded_path = str(urllib.parse.quote(path, safe="/:"))
    return url_encoded_path.replace("%2520", "%20")  # Handle edge cases.


def ensure_windows_file_path_format_encoding_as_url(path: str) -> str:
    """Relevant for Windows where a file path name should be "file://path/to/file.html" instead of "file://path\\to\\file.html" ."""

    output = path.replace("\\", "/")  # Raw replace backslash with slash.
    # Handle exception for "file:///C:/path/to/file.html" declaration in URLs:
    if re.match(r"^file:/+[A-Za-z]:", output, re.IGNORECASE):
        output = re.sub(r"^file:/+", "file:///", output, flags=re.IGNORECASE)
    return encode_path_as_url(output)


def get_entries(path: FilePath) -> list[str]:
    """Get all file and directory names in a directory."""

    return os.listdir(path)


def update_path_format_if_windows(path: str) -> str:
    return ensure_windows_file_path_format_encoding_as_url(path) if operating_system.is_windows() else encode_path_as_url(path)
