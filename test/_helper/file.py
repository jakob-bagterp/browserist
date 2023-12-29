import os
from pathlib import Path


def create(file_path: str | Path) -> None:
    """Create test file."""

    with open(file_path, "w") as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")


def create_multiple(dir_path: str, file_exension: str, amount: int) -> None:
    """Create test files with a certain file extension (e.g. `zip`, `txt`, etc.) in a given directory path, e.g. `downloads/file_1.zip`, `downloads/file_2.zip`, etc."""

    for i in range(amount):
        file_path = os.path.join(dir_path, f"file_{i}.{file_exension}")
        create(file_path)


def download_dir_and_file_path_controller(has_file: bool, temp_dir_path: str) -> tuple[str, str, str]:
    """Controller for testing of temporary download directory and file.

    Returns:
        tuple[str, str, str]: download_dir, file_name, file_path
    """

    download_dir = os.path.join(temp_dir_path, "downloads")
    os.makedirs(download_dir)
    file_name = "file.txt"
    file_path = os.path.join(download_dir, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    if has_file:
        create(file_path)
    return download_dir, file_name, file_path
