import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/h1", True),
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", True),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[1]/div/h1", True),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/footer", True),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[14]/h2", True),
    (internal_url.W3SCHOOLS_COM, "//*[@id='google_translate_element']", False),
])
def test_check_if_is_element_displayed(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.check_if.is_element_displayed(xpath) is expected
