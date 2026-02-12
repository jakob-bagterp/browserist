from pathlib import Path

import _helper
import pytest

from browserist import helper
from browserist.model.type.path import FilePath


@pytest.mark.parametrize("has_file, expected_file_exists", [(False, False), (True, True), (None, False)])
def test_helper_file_exists(has_file: bool, expected_file_exists: bool, tmpdir: Path) -> None:
    _, _, file_path = _helper.file.download_dir_and_file_path_controller(has_file, str(tmpdir))
    file_path = FilePath(file_path)
    assert helper.file.exists(file_path) == expected_file_exists
