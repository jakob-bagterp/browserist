from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

def test_get_url_from_link() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        assert browser.get.url.from_link("/html/body/div/p[2]/a") == "https://www.iana.org/domains/example"
