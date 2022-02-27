import pytest

from browserist import helper


@pytest.mark.parametrize("path, expected", [
    ("file://path\\to\\file.html", "file://path/to/file.html"),
    ("file:///path\\to\\file.html", "file:///path/to/file.html"),
    ("file://C:path\\to\\file.html", "file:///C:path/to/file.html"),
    ("file:///C:path\\to\\file.html", "file:///C:path/to/file.html"),
])
def test_helper_ensure_path_format_encoding_as_url(path: str, expected: str) -> None:
    assert helper.directory.ensure_path_format_encoding_as_url(path) == expected
