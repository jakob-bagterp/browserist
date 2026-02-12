import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_meta_description",
    [
        (internal_url.MINI_SITE_HOMEPAGE, "Discover the best products for your needs"),
        (internal_url.MINI_SITE_FEATURE_1, "Feature 1"),
        (internal_url.SEARCH, ""),  # Doesn't have any meta description.
    ],
)
def test_get_meta_description(url: str, expected_meta_description: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.meta_description() == expected_meta_description
