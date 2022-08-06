import pytest
from _mock_data.url import internal_url

from browserist import Browser, image_helper


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div[3]/a[1]/i", False),
    ("//*[@id='bgcodeimg2']/div/img", True),
    ("//*[@id='Frontend']/img", True),
    ("//*[@id='Backend']/img", True),
])
def test_is_element_loaded(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    element = browser.get.element(xpath)
    assert image_helper.is_element_loaded(browser.driver, element) is expected
