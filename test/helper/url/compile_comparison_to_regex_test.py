import pytest

from browserist import helper
from browserist.model.type.url import URL

IGNORE_TRAILING_SLASH_DEFAULT = True
IGNORE_PARAMETERS_DEFAULT = False
IGNORE_HTTPS_DEFAULT = False


@pytest.mark.parametrize("url, url_comparison, expected", [
    ("https://example.com", "https://example.com/", True),
    ("https://example.com/", "https://example.com/", True),
    ("https://example.com?page=1", "https://example.com?page=1", True),
    ("https://example.com?page=1", "https://example.com/?page=1", True),
])
def test_helper_url_compile_comparison_to_regex_default(url: str, url_comparison: str, expected: bool) -> None:
    url = URL(url)
    url_comparison_regex = helper.url.compile_comparison_to_regex(url, IGNORE_TRAILING_SLASH_DEFAULT, IGNORE_PARAMETERS_DEFAULT, IGNORE_HTTPS_DEFAULT)
    assert bool(url_comparison_regex.match(url_comparison)) is expected


@pytest.mark.parametrize("url, url_comparison, ignore_https, expected", [
    ("http://example.com", "https://example.com", True, True),
    ("http://example.com", "https://example.com", False, False),
    ("http://example.com/", "https://example.com", True, True),
    ("http://example.com/", "https://example.com", False, False),
    ("https://example.com", "https://example.com", True, True),
    ("https://example.com", "https://example.com", False, True),
])
def test_helper_url_compile_comparison_to_regex_ignore_https(url: str, url_comparison: str, ignore_https: bool, expected: bool) -> None:
    url = URL(url)
    url_comparison_regex = helper.url.compile_comparison_to_regex(url, IGNORE_TRAILING_SLASH_DEFAULT, IGNORE_PARAMETERS_DEFAULT, ignore_https)
    assert bool(url_comparison_regex.match(url_comparison)) is expected
