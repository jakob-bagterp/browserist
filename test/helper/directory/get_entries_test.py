import os
from pathlib import Path

import _helper

from browserist import helper
from browserist.model.type.path import FilePath


def test_helper_directory_get_entries(tmpdir: Path) -> None:
    NUMBER_OF_DIRECTORIES = 4
    NUMBER_OF_FILES = 3
    download_dir = FilePath(os.path.join(str(tmpdir), "downloads"))

    _helper.directory.create_multiple(download_dir, NUMBER_OF_DIRECTORIES)
    download_dir_entries = helper.directory.get_entries(download_dir)
    assert len(download_dir_entries) == NUMBER_OF_DIRECTORIES

    _helper.file.create_multiple(download_dir, "txt", NUMBER_OF_FILES)
    download_dir_entries = helper.directory.get_entries(download_dir)
    assert len(download_dir_entries) == NUMBER_OF_DIRECTORIES + NUMBER_OF_FILES
