import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.feature_1 import (
    MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH,
    MINI_SITE_FEATURE_1_IMAGE_1_XPATH,
)

from browserist import Browser


@pytest.mark.parametrize(
    "xpath, expected",
    [
        (MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH, True),
        (MINI_SITE_FEATURE_1_IMAGE_1_XPATH, False),
        (does_not_exist.XPATH, False),
    ],
)
def test_check_if_contains_any_text(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    assert browser.check_if.contains_any_text(xpath) is expected
