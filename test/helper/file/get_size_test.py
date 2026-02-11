import os
from pathlib import Path

import _helper
from _helper import directory

from browserist import helper
from browserist.model.type.path import FilePath


def test_helper_file_get_size(tmpdir: Path) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    file_path = FilePath(os.path.join(download_dir, "file.txt"))
    _helper.file.create(file_path)
    assert helper.file.get_size(file_path) == 56
