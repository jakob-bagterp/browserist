from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

class TestGetTextFromElement():
    def test_get_text_from_element(self) -> None:
        with Browser(default.HEADLESS) as browser:
            browser.open.url(internal_url.EXAMPLE_COM)
            assert browser.get.text.from_element("/html/body/div/p[2]") == "More information..."
