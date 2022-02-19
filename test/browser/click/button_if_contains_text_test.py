import pytest
from browserist import Browser
from _helper import external_url, internal_url

@pytest.mark.parametrize("text, ignore_case", [
    ("More information", False),
    ("mOrE iNforMatiOn", True)
])
def test_click_button_if_contains_text(text: str, ignore_case: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.click.button_if_contains_text("/html/body/div/p[2]/a", text, ignore_case)
    browser.wait.until_url_contains(external_url.IANA_ORG)
    assert browser.get.url.current() == external_url.IANA_ORG
