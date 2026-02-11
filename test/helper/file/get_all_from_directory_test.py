import os
from pathlib import Path

import _helper

from browserist import helper
from browserist.model.type.path import FilePath


def test_helper_file_get_all_from_directory(tmpdir: Path) -> None:
    NUMBER_OF_DIRECTORIES = 3
    NUMBER_OF_XYZ_FILES = 2
    NUMBER_OF_TXT_FILES = 4
    download_dir = FilePath(os.path.join(str(tmpdir), "downloads"))

    _helper.directory.create_multiple(download_dir, NUMBER_OF_DIRECTORIES)
    download_dir_entries = helper.directory.get_entries(download_dir)
    assert len(download_dir_entries) == NUMBER_OF_DIRECTORIES

    _helper.file.create_multiple(download_dir, "xyz", NUMBER_OF_XYZ_FILES)
    download_dir_entries = helper.directory.get_entries(download_dir)
    assert len(download_dir_entries) == NUMBER_OF_DIRECTORIES + NUMBER_OF_XYZ_FILES

    _helper.file.create_multiple(download_dir, "txt", NUMBER_OF_TXT_FILES)
    download_dir_entries = helper.directory.get_entries(download_dir)
    assert len(download_dir_entries) == NUMBER_OF_DIRECTORIES + NUMBER_OF_XYZ_FILES + NUMBER_OF_TXT_FILES

    all_txt_files = helper.file.get_all_from_directory(download_dir, "txt")
    assert len(all_txt_files) == NUMBER_OF_TXT_FILES
