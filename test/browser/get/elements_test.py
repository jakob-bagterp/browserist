import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_count",
    [
        (internal_url.MINI_SITE_HOMEPAGE, "//h1", 1),
        (internal_url.MINI_SITE_HOMEPAGE, "//h3", 3),
        (internal_url.MINI_SITE_HOMEPAGE, "//a", 9),
        (internal_url.MINI_SITE_FEATURE_1, "//h1", 1),
        (internal_url.MINI_SITE_FEATURE_1, "//p", 8),
    ],
)
def test_get_elements(url: str, xpath: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    elements = browser.get.elements(xpath)
    assert len(elements) == expected_count
