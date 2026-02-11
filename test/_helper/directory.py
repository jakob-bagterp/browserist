import os
from pathlib import Path


def create(dir_path: str) -> None:
    """Create directory."""

    os.makedirs(dir_path)


def create_multiple(base_dir_path: str, amount: int) -> None:
    """Create test sub directories in a given base directory, e.g. `downloads/subdir_1`, `downloads/subdir_2`, etc."""

    for i in range(amount):
        subdir_path = os.path.join(base_dir_path, f"subdir_{i}")
        create(subdir_path)


def get_path_for_web_mock_data() -> str:
    path_of_this_file = Path(__file__)
    path_of_static_directory = path_of_this_file.parent.parent.resolve()
    return f"{path_of_static_directory}/_mock_data/web"


def create_and_get_temporary(tmpdir: Path, dir_name: str) -> str:
    """Create temporary directory with `tmpdir` fixture and return path."""

    return str(tmpdir.mkdir(dir_name))


def create_and_get_temporary_download_dir(tmpdir: Path) -> str:
    """Create temporary download directory with `tmpdir` fixture and return path."""

    return create_and_get_temporary(tmpdir, "downloads")
