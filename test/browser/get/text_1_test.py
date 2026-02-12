import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import (
    MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH,
    MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH,
)

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_text",
    [
        (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "Learn more"),
        (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH, "Welcome"),
        (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/h2[1]", "Suspendisse vitae nibh ipsum"),
    ],
)
def test_get_text(url: str, xpath: str, expected_text: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.text(xpath) == expected_text
