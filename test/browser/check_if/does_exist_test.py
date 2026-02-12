import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "xpath, expected", [(MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH, True), (does_not_exist.XPATH, False)]
)
def test_check_if_does_exist(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    assert browser.check_if.does_exist(xpath) is expected
