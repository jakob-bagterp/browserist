import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH, True),
    (internal_url.MINI_SITE_FEATURE_1, "//div[@id='main']//img[1]", True),
])
def test_get_element(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert bool(browser.get.element(xpath)) is expected
