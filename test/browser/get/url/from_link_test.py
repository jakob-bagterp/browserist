import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_url", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", "https://www.iana.org/domains/example"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a[3]",
     "https://www.w3schools.com/tags/default.asp"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[6]/div/div[1]/a[1]", "https://www.w3schools.com/sql/default.asp"),
])
def test_get_url_from_link(url: str, xpath: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.from_link(xpath) == expected_url
