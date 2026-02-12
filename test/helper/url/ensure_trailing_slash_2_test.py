import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url, expected_url",
    [
        ("http://example.com", "http://example.com/"),
        ("http://example.com/", "http://example.com/"),
        ("http://example.com?page=1", "http://example.com?page=1"),
        ("http://example.com/?page=1", "http://example.com/?page=1"),
    ],
)
def test_helper_url_ensure_trailing_slash(url: str, expected_url: str) -> None:
    assert helper.url.ensure_trailing_slash(url) == expected_url
