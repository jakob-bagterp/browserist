import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[1]/div/h1", True),
    (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[2]/div[1]/a", True),
    (internal_url.MINI_SITE_HOMEPAGE, does_not_exist.XPATH, False),
    (internal_url.MINI_SITE_FEATURE_1, "//header", True),
    (internal_url.MINI_SITE_FEATURE_1, "//div[@id='main']", True),
    (internal_url.MINI_SITE_FEATURE_1, "//div[@id='main']//h2[1]", True),
    (internal_url.MINI_SITE_FEATURE_1, "//*[@id='does_not_exist']", False),
    (internal_url.MINI_SITE_FEATURE_1, does_not_exist.XPATH, False),
])
def test_check_if_is_displayed(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.check_if.is_displayed(xpath) is expected
