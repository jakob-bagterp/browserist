import pytest

from browserist import helper

IGNORE_TRAILING_SLASH_DEFAULT = True
IGNORE_PARAMETERS_DEFAULT = False
IGNORE_HTTPS_DEFAULT = False


@pytest.mark.parametrize(
    "url, url_comparison, expected",
    [
        ("https://example.com", "https://example.com/", True),
        ("https://example.com/", "https://example.com/", True),
        ("https://example.com?page=1", "https://example.com?page=1", True),
        ("https://example.com?page=1", "https://example.com/?page=1", True),
    ],
)
def test_helper_url_compile_comparison_to_regex_pattern_default(url: str, url_comparison: str, expected: bool) -> None:
    url_pattern = helper.url.compile_comparison_to_regex_pattern(
        url, IGNORE_TRAILING_SLASH_DEFAULT, IGNORE_PARAMETERS_DEFAULT, IGNORE_HTTPS_DEFAULT
    )
    assert bool(url_pattern.fullmatch(url_comparison)) is expected


@pytest.mark.parametrize(
    "url, url_comparison, ignore_trailing_slash, expected",
    [
        ("https://example.com", "https://example.com/", True, True),
        ("https://example.com/", "https://example.com/", True, True),
        ("https://example.com", "https://example.com/", False, False),
        ("https://example.com/", "https://example.com/", False, True),
        ("https://example.com?page=1", "https://example.com?page=1", True, True),
        ("https://example.com?page=1", "https://example.com?page=1", False, True),
        ("https://example.com?page=1", "https://example.com/?page=1", True, True),
        ("https://example.com?page=1", "https://example.com/?page=1", False, False),
    ],
)
def test_helper_url_compile_comparison_to_regex_pattern_ignore_trailing_slash(
    url: str, url_comparison: str, ignore_trailing_slash: bool, expected: bool
) -> None:
    url_pattern = helper.url.compile_comparison_to_regex_pattern(
        url, ignore_trailing_slash, IGNORE_PARAMETERS_DEFAULT, IGNORE_HTTPS_DEFAULT
    )
    assert bool(url_pattern.fullmatch(url_comparison)) is expected


@pytest.mark.parametrize(
    "url, url_comparison, ignore_https, expected",
    [
        ("http://example.com", "https://example.com", True, True),
        ("http://example.com", "https://example.com", False, False),
        ("http://example.com/", "https://example.com", True, True),
        ("http://example.com/", "https://example.com", False, False),
        ("https://example.com", "https://example.com", True, True),
        ("https://example.com", "https://example.com", False, True),
    ],
)
def test_helper_url_compile_comparison_to_regex_pattern_ignore_https(
    url: str, url_comparison: str, ignore_https: bool, expected: bool
) -> None:
    url_pattern = helper.url.compile_comparison_to_regex_pattern(
        url, IGNORE_TRAILING_SLASH_DEFAULT, IGNORE_PARAMETERS_DEFAULT, ignore_https
    )
    assert bool(url_pattern.fullmatch(url_comparison)) is expected
