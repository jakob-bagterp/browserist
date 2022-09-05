import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("//*[@id='main']/div[1]/div/h1", True),
    ("//*[@id='main']/footer", False),
    ("//*[@name=\"can't handle mix of single and double quotes\"]", False),
    (does_not_exist.XPATH, False),
])
def test_check_if_is_in_viewport(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.check_if.is_in_viewport(xpath) is expected
