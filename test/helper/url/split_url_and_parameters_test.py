import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url, expected_url, expected_parameters",
    [
        ("https://example.com", "https://example.com", ""),
        ("https://example.com/", "https://example.com/", ""),
        ("https://example.com/#page-1", "https://example.com/#page-1", ""),
        ("https://example.com?page=1", "https://example.com", "?page=1"),
        ("https://example.com/?page=1", "https://example.com/", "?page=1"),
        ("https://example.com/?page=1&test=True", "https://example.com/", "?page=1&test=True"),
        ("https://example.com/?page=1?test=True", "https://example.com/", "?page=1?test=True"),
        ("https://example.com/search?query=test&page=1", "https://example.com/search", "?query=test&page=1"),
        ("https://example.com/search/?query=test&page=1", "https://example.com/search/", "?query=test&page=1"),
    ],
)
def test_helper_url_split_url_and_parameters(url: str, expected_url: str, expected_parameters: str) -> None:
    url, parameters = helper.url.split_url_and_parameters(url)
    assert url == expected_url
    assert parameters == expected_parameters
