from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

class TestGetPageTitle():
    def test_get_page_title(self) -> None:
        with Browser(default.HEADLESS) as browser:
            browser.open.url(internal_url.EXAMPLE_COM)
            assert browser.get.page_title() == "Example Domain"
