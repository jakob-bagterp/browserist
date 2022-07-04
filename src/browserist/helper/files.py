import os


def remove(file_paths: str | list[str]) -> None:
    for file_path in file_paths:
        os.remove(file_path)


def find(directory: str, file_name_snippet: str) -> list[str]:
    pass
