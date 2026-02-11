import os
from pathlib import Path


def image_has_minimum_file_size(directory: str | Path, file_name: str, minimum_file_size: int) -> bool:
    file_path = os.path.join(str(directory), file_name)
    return os.path.getsize(file_path) > minimum_file_size


def images_have_minimum_file_size(directory: str | Path, minimum_file_size: int) -> bool:
    def absolute_path(file: str) -> str:
        return os.path.join(directory, file)

    directory = str(directory)
    files = [absolute_path(file) for file in os.listdir(directory) if os.path.isfile(absolute_path(file))]
    return all(os.path.getsize(file) > minimum_file_size for file in files)
