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
    _, file_path = _helper.file.download_dir_and_file_path_controller(has_file, tmpdir)
    file_path = FilePath(file_path)
    assert helper.file.exists(file_path) == expected_file_exists
