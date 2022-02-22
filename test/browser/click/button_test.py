from _helper import external_url
from _helper import internal_url

from browserist import Browser


def test_click_button(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url_if_not_current(internal_url.EXAMPLE_COM)
    browser.click.button("/html/body/div/p[2]/a")
    browser.wait.until_url_contains(external_url.IANA_ORG)
    assert browser.get.url.current() == external_url.IANA_ORG
