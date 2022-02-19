from browserist import Browser
from _helper import internal_url

def test_get_url_from_link(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.get.url.from_link("/html/body/div/p[2]/a") == "https://www.iana.org/domains/example"
