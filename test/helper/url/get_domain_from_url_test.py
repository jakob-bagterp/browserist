import pytest

from browserist import helper


@pytest.mark.parametrize(
    "url, expected_domain",
    [
        ("http://example.com", "example.com"),
        ("https://www.example.com/", "www.example.com"),
        ("https://abc.xyz.com/some/page", "abc.xyz.com"),
    ],
)
def test_get_domain_from_url(url: str, expected_domain: str) -> None:
    assert helper.url.get_domain_from_url(url) == expected_domain
