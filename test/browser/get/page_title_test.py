import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_title",
    [(internal_url.MINI_SITE_HOMEPAGE, "Homepage"), (internal_url.MINI_SITE_FEATURE_1, "Feature 1")],
)
def test_get_page_title(url: str, expected_title: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.page_title() == expected_title
