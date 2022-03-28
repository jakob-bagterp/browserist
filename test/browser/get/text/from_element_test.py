import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]", "More information..."),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a[1]", "Try Frontend Editor (HTML/CSS/JS)"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/h1", "W3Schools Spaces"),
])
def test_get_text_from_element(url: str, xpath: str, expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.text.from_element(xpath) == expected
