import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/h1", True),  # Headline always displayed.
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", True),  # Link always displayed.
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[1]/div/h1", True),  # Headline always displayed.
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/footer", True),  # Footer displayed, though you have to scroll down.
    # Headline displayed, though you have to scroll down.
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[14]/h2", True),
    (internal_url.W3SCHOOLS_COM, "//*[@id='google_translate_element']", False),  # Is "display: none" in inline styling.
])
def test_check_if_is_element_displayed(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.check_if.is_element_displayed(xpath) is expected
