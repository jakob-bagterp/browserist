import pytest
from _helper.url import internal_url

from browserist import Browser
from browserist.helper.directory import update_path_format_if_windows


@pytest.mark.parametrize("url, xpath, attribute, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", "href", "https://www.iana.org/domains/example"),
    (internal_url.EXAMPLE_COM, "/html/head/meta[3]", "name", "viewport"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/img", "src",
     update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png")),
    (internal_url.W3SCHOOLS_COM, "/html/head/meta[4]", "content",
     "Well organized and easy to understand Web building tutorials with lots of examples of how to use HTML, CSS, JavaScript, SQL, Python, PHP, Bootstrap, Java, XML and more."),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[8]/div/div[30]", "class", "w3-col l6 s12 w3-center"),
])
def test_get_attribute_value(url: str, xpath: str, attribute: str, expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.attribute.value(xpath, attribute) == expected
