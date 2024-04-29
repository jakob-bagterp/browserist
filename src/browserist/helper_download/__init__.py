import os
from pathlib import Path

from ..model.browser.base.driver import BrowserDriver
from ..model.type.path import FilePath


def get_file_path(browser_driver: BrowserDriver, file_name: str | Path) -> FilePath:
    file_path = os.path.join(browser_driver.settings._download_dir, file_name)
    return FilePath(file_path)


def add_file_extension(file_name: str, file_extension: str) -> str:
    """Add a file extension to a file name.

    Args:
        expected_file_name (str): For example, `file.txt`.
        temporary_file_extension (str): For example, `.download`.

    Returns:
        For example `file.txt.download`.
    """

    return f"{file_name}{file_extension}"


def remove_file_extension(file_name: str, file_extension: str) -> str:
    """Remove a file extension from a file name.

    Args:
        expected_file_name (str): For example, `file.txt.download`.
        temporary_file_extension (str): For example, `.download`.

    Returns:
        For example `file.txt`.
    """

    return file_name.rstrip(file_extension)
