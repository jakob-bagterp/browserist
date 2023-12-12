import os

from py.path import local


def create(file_path: str) -> None:
    """Create test file."""

    with open(file_path, "w") as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")


def download_dir_and_file_path_controller(temp_dir: local, has_file: bool) -> tuple[str, str]:
    download_dir = os.path.join(str(temp_dir), "downloads")
    os.mkdir(download_dir)
    file_path = os.path.join(download_dir, "file.txt")
    if has_file:
        create(file_path)
    return download_dir, file_path
