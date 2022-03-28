import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", ["https://www.iana.org/domains/example"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a[3]",
     ["https://www.w3schools.com/tags/default.asp"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a", ["https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello",
     "https://www.w3schools.com/tryit/trycompiler.asp?filename=demo_python"]),
])
def test_get_url_from_multiple_links(url: str, xpath: str, expected: list[str], browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.from_multiple_links(xpath) == expected
