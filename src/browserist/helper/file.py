import os
import shutil


def remove(file_paths: str | list[str]) -> None:
    for file_path in file_paths:
        os.remove(file_path)


def copy(source: str, destination: str) -> None:
    shutil.copy(source, destination)
