import pytest

from browserist import helper


@pytest.mark.parametrize("directory, expected", [
    ("some/directory", "some/directory/"),
    ("some/directory/", "some/directory/"),
    ("/some/directory", "/some/directory/"),
    ("/some/directory/", "/some/directory/"),
    ("./some/directory", "./some/directory/"),
    ("./some/directory/", "./some/directory/"),
])
def test_helper_directory_ensure_trailing_slash(directory: str, expected: str) -> None:
    assert helper.directory.ensure_trailing_slash(directory) == expected
