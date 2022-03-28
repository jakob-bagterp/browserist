import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div/p[2]/a", True),
    ("/html/body/div/h1/div", False),  # Element doesn't exist.
    ("/html/body/div/h1", True),
])
def test_check_if_is_element_clickable(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.check_if.is_element_clickable(xpath) is expected
