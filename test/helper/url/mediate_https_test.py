import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url1_in, url2_in, url1_out, url2_out",
    [
        ("http://example.com", "http://example.com/", "http://example.com", "http://example.com/"),
        ("https://example.com", "http://example.com/", "https://example.com", "https://example.com/"),
        ("http://example.com", "https://example.com/", "https://example.com", "https://example.com/"),
        ("https://example.com", "https://example.com/", "https://example.com", "https://example.com/"),
    ],
)
def test_helper_url_mediate_https(url1_in: str, url2_in: str, url1_out: str, url2_out: str) -> None:
    assert helper.url.mediate_https(url1_in, url2_in) == (url1_out, url2_out)
