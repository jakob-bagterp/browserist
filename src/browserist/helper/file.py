import asyncio
import os
import shutil
from contextlib import suppress

from ..model.type.path import FilePath
from . import directory


def remove(file_paths: FilePath | list[FilePath]) -> None:
    for file_path in file_paths:
        os.remove(file_path)


async def async_remove(file_paths: FilePath | list[FilePath]) -> None:
    await asyncio.gather(*[asyncio.to_thread(os.remove, file_path) for file_path in file_paths])


def copy(source: str, destination: str) -> None:
    shutil.copy(source, destination)


def exists(file_path: FilePath | None) -> bool:
    return False if file_path is None else os.path.exists(file_path)


def is_file(path: FilePath, file_name: str) -> bool:
    file_path = os.path.join(path, file_name)
    return os.path.isfile(file_path)


def get_all_from_directory(path: FilePath, file_extension: str | None = None) -> list[str]:
    """Get all file names in a directory, eventually filtered by a specific file type.

    Args:
        path (FilePath): Path to the directory.
        file_extension (str | None, optional): Filter by file extension, e.g. `txt`.

    Returns:
        List of file names.
    """

    files_and_folders = directory.get_entries(path)
    if file_extension:
        return [file for file in files_and_folders if is_file(path, file) and file.endswith(f".{file_extension}")]
    else:
        return [file for file in files_and_folders if is_file(path, file)]


def get_size(file_path: FilePath, suppress_file_not_found_error: bool = False) -> int:  # type: ignore
    """Get size of file in bytes."""

    if suppress_file_not_found_error:
        with suppress(FileNotFoundError):
            return os.path.getsize(file_path)
    else:
        return os.path.getsize(file_path)
