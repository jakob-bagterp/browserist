import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_urls", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", ["https://www.iana.org/domains/example"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a[3]",
     ["https://www.w3schools.com/tags/default.asp"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a", ["https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello",
     "https://www.w3schools.com/tryit/trycompiler.asp?filename=demo_python"]),
])
def test_get_url_from_links(url: str, xpath: str, expected_urls: list[str], browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.from_links(xpath) == expected_urls
