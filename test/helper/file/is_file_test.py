import os

import _helper

from browserist import helper


def test_helper_file_is_file(tmpdir) -> None:
    NUMBER_OF_DIRECTORIES = 3
    NUMBER_OF_FILES = 2
    download_dir = os.path.join(str(tmpdir), "downloads")

    _helper.directory.create_multiple(download_dir, NUMBER_OF_DIRECTORIES)
    assert len(helper.directory.get_entries(download_dir)) == NUMBER_OF_DIRECTORIES

    _helper.file.create_multiple(download_dir, "txt", NUMBER_OF_FILES)
    assert len(helper.directory.get_entries(download_dir)) == NUMBER_OF_DIRECTORIES + NUMBER_OF_FILES

    download_dir_entries = helper.directory.get_entries(download_dir)
    download_dir_files = [file_name for file_name in download_dir_entries if helper.file.is_file(download_dir, file_name)]
    assert len(download_dir_files) == NUMBER_OF_FILES
