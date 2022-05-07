import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, attribute, expected", [
    (internal_url.EXAMPLE_COM, "//a", "href", ["https://www.iana.org/domains/example"]),
    (internal_url.EXAMPLE_COM, "/html/head/meta[3]", "name", ["viewport"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a", "href", [
     "https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello",
     "https://www.w3schools.com/tryit/trycompiler.asp?filename=demo_python"]),
])
def test_get_attribute_values(url: str, xpath: str, attribute: str, expected: list[str], browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.attribute.values(xpath, attribute) == expected
