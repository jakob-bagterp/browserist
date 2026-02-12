import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url, expected_url",
    [
        ("http://example.com", "http://example.com"),
        ("http://example.com/", "http://example.com/"),
        ("http://example.com?page=1", "http://example.com"),
        ("http://example.com/?page=1", "http://example.com/"),
        ("http://example.com/?page=1&test=True", "http://example.com/"),
        ("http://example.com/?page=1?test=True", "http://example.com/"),
    ],
)
def test_helper_url_remove_parameters(url: str, expected_url: str) -> None:
    assert helper.url.remove_parameters(url) == expected_url
