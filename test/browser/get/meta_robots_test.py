import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_meta_robots",
    [
        (internal_url.MINI_SITE_HOMEPAGE, "noindex"),
        (internal_url.MINI_SITE_FEATURE_1, "index, follow"),
        (internal_url.SEARCH, ""),  # Doesn't have any meta robots specified.
    ],
)
def test_get_meta_robots(url: str, expected_meta_robots: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.meta_robots() == expected_meta_robots
