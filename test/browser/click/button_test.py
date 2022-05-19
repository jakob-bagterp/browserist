import pytest
from _mock_data.url import external_url, internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, url_expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", external_url.IANA_ORG),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a[1]",
     "https://www.w3schools.com/html/default.asp"),
])
def test_click_button(url: str, xpath: str, url_expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    browser.click.button(xpath)
    browser.wait.until.url.contains(url_expected)
    assert browser.get.url.current() == url_expected
