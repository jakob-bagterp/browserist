import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize("text, ignore_case", [("Learn more", False), ("lEArN MoRE", True)])
def test_click_button_if_contains_text(text: str, ignore_case: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.click.button_if_contains_text(MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, text, ignore_case)
    browser.wait.until.url.contains(internal_url.MINI_SITE_FEATURE_1)
    assert browser.get.url.current() == internal_url.MINI_SITE_FEATURE_1
