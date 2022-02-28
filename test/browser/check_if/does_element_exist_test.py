import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div/p[2]/a", True),
    ("/html/body/div/p[2]/a/div", False),
])
def test_check_if_does_element_exist(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.check_if.does_element_exist(xpath) is expected
