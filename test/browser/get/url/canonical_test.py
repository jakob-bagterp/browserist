import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_canonical_url",
    [
        (internal_url.MINI_SITE_HOMEPAGE, "https://example.com/homepage.html"),
        (internal_url.MINI_SITE_FEATURE_1, "https://example.com/feature/1.html"),
        (internal_url.SEARCH, None),  # Doesn't have any canonical URL specified.
    ],
)
def test_get_canonical_ur(url: str, expected_canonical_url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.canonical() == expected_canonical_url
