import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url, expected",
    [
        ("http://example.com", False),
        ("https://example.com/", False),
        ("https://example.com/#page-1", False),
        ("https://example.com/?page=1", True),
        ("https://example.com?page=1", True),
        ("https://example.com/search", False),
        ("https://example.com/search?query=test&page=1", True),
        ("https://example.com/search/?query=test&page=1", True),
    ],
)
def test_helper_url_has_parameters(url: str, expected: bool) -> None:
    assert helper.url.has_parameters(url) is expected
