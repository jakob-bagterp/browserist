import pytest

from browserist import helper


@pytest.mark.parametrize("directory, expected_directory_path", [
    ("some/directory", "some/directory/"),
    ("some/directory/", "some/directory/"),
    ("/some/directory", "/some/directory/"),
    ("/some/directory/", "/some/directory/"),
    ("./some/directory", "./some/directory/"),
    ("./some/directory/", "./some/directory/"),
])
def test_helper_directory_ensure_trailing_slash(directory: str, expected_directory_path: str) -> None:
    assert helper.directory.ensure_trailing_slash(directory) == expected_directory_path
