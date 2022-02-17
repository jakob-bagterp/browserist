from browserist import Browser
from _config.browser_settings import default
from _helper import external_url, internal_url

def click_button_if_contains_text(text: str, ignore_case: bool) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        browser.click.button_if_contains_text("/html/body/div/p[2]/a", text, ignore_case)
        browser.wait.until_url_contains(external_url.IANA_ORG)
        assert browser.get.url.current() == external_url.IANA_ORG

class TestClickButtonIfContainsText():
    def test_click_button_if_contains_text_1(self) -> None:
        click_button_if_contains_text("More information", ignore_case = False)

    def test_click_button_if_contains_text_2(self) -> None:
        click_button_if_contains_text("mOrE iNforMatiOn", ignore_case = True)
