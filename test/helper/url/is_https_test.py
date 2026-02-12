import pytest

from browserist import helper


@pytest.mark.parametrize("url, expected", [("http://example.com", False), ("https://example.com/", True)])
def test_helper_url_is_https(url: str, expected: bool) -> None:
    assert helper.url.is_https(url) == expected
