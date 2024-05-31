import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_url", [
    (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, internal_url.MINI_SITE_FEATURE_1),
    (internal_url.MINI_SITE_HOMEPAGE, "/html/body/header/nav/ul/li[2]/a", internal_url.MINI_SITE_ABOUT),
])
def test_click_button(url: str, xpath: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    browser.click.button(xpath)
    browser.wait.until.url.contains(expected_url)
    assert browser.get.url.current() == expected_url
