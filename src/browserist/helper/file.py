import asyncio
import os
import shutil

from ..model.type.path import FilePath


def remove(file_paths: FilePath | list[FilePath]) -> None:
    for file_path in file_paths:
        os.remove(file_path)


async def async_remove(file_paths: FilePath | list[FilePath]) -> None:
    await asyncio.gather(*[asyncio.to_thread(os.remove, file_path) for file_path in file_paths])


def copy(source: str, destination: str) -> None:
    shutil.copy(source, destination)
