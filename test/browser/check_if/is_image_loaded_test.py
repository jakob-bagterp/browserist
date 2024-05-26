import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/section[1]/div/h1", False),
    ("//*[@id='main']/img[1]", True),
    (does_not_exist.XPATH, False),
])
def test_check_if_is_image_loaded(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    assert browser.check_if.is_image_loaded(xpath) is expected
