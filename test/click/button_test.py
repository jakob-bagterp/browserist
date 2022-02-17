from browserist import Browser
from _config.browser_settings import default
from _helper import external_url, internal_url

class TestClickButton():
    def test_click_button(self) -> None:
        with Browser(default.HEADLESS) as browser:
            browser.open.url(internal_url.EXAMPLE_COM)
            browser.click.button("/html/body/div/p[2]/a")
            browser.wait.until_url_contains(external_url.IANA_ORG)
            assert browser.get.url.current() == external_url.IANA_ORG
