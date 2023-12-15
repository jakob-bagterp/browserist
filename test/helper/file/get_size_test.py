import os

import _helper
from py.path import local

from browserist import helper
from browserist.model.type.path import FilePath


def test_helper_file_get_size(tmpdir: local) -> None:
    download_dir = FilePath(os.path.join(str(tmpdir), "downloads"))
    _helper.directory.create(download_dir)
    file_path = FilePath(os.path.join(download_dir, "file.txt"))
    _helper.file.create(file_path)
    assert helper.file.get_size(file_path) == 56
