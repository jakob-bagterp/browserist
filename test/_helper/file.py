import os


def create(file_path: str) -> None:
    """Create test file."""

    with open(file_path, "w") as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")


def download_dir_and_file_path_controller(has_file: bool, temp_dir_path: str) -> tuple[str, str]:
    download_dir = os.path.join(temp_dir_path, "downloads")
    os.mkdir(download_dir)
    file_path = os.path.join(download_dir, "file.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
    if has_file:
        create(file_path)
    return download_dir, file_path
