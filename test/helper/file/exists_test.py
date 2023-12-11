import os

import pytest
from py.path import local

from browserist import helper
from browserist.model.type.path import FilePath


@pytest.mark.parametrize("directory, file_name, expected", [
    ("downloads", "file.txt", True),
    ("downloads", None, False),
])
def test_helper_file_exists(directory: str, file_name: str | None, expected: bool, tmpdir: local) -> None:
    base_dir = os.path.join(str(tmpdir), directory)
    os.mkdir(base_dir)
    if file_name:
        file_path = os.path.join(base_dir, file_name)
        with open(file_path, "w") as file:
            file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    else:
        file_path = "non_existent_file_path"
    file_path = FilePath(file_path)
    assert helper.file.exists(file_path) == expected
