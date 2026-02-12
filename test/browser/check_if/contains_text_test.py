import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "xpath, regex, ignore_case, expected",
    [
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "Learn more", False, True),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "More", False, False),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, r"^learn", True, True),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, r"^learn", False, False),
        (does_not_exist.XPATH, "does not matter", True, False),
    ],
)
def test_check_if_contains_text(
    xpath: str, regex: str, ignore_case: bool, expected: bool, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    assert browser.check_if.contains_text(xpath, regex, ignore_case) is expected
