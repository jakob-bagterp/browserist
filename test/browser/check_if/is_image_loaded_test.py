import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div[3]/a[1]/i", False),
    ("//*[@id='bgcodeimg2']/div/img", True),
    ("//*[@id='Frontend']/img", True),
    ("//*[@id='Backend']/img", True),
    (does_not_exist.XPATH, False),
])
def test_check_if_is_image_loaded(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.check_if.is_image_loaded(xpath) is expected
