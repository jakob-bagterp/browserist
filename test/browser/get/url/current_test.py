from _helper import external_url

from browserist import Browser

def test_get_current_url(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(external_url.EXAMPLE_COM)
    assert browser.get.url.current() == "http://example.com/"
