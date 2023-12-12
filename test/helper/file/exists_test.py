import os

import _helper
import pytest
from py.path import local

from browserist import helper
from browserist.model.type.path import FilePath


@pytest.mark.parametrize("has_file, expected_file_exists", [
    (False, False),
    (True, True),
])
def test_helper_file_exists(has_file: bool, expected_file_exists: bool, tmpdir: local) -> None:
    downloads_dir = os.path.join(str(tmpdir), "downloads")
    os.mkdir(downloads_dir)
    file_path = os.path.join(downloads_dir, "file.txt")
    if has_file:
        _helper.file.create(file_path)
    file_path = FilePath(file_path)
    assert helper.file.exists(file_path) == expected_file_exists
