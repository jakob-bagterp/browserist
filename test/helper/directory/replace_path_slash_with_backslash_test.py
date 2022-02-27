import pytest

from browserist import helper


@pytest.mark.parametrize("path, expected", [
    ("file://path/to/file.html", "file://path\\to\\file.html"),
    ("file:///path/to/file.html", "file:///path\\to\\file.html"),
    ("file://C:path/to/file.html", "file://C:path\\to\\file.html"),
    ("file:///C:path/to/file.html", "file:///C:path\\to\\file.html"),
])
def test_helper_replace_path_slash_with_backslash(path: str, expected: str) -> None:
    assert helper.directory.replace_path_slash_with_backslash(path) == expected
