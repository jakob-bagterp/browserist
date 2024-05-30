import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/section[1]/div/h1", True),
    ("//*[@id='main']/img[1]", False),
    (does_not_exist.XPATH, False),
])
def test_check_if_contains_any_text(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    assert browser.check_if.contains_any_text(xpath) is expected
