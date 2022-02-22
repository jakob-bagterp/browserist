from _helper import internal_url

from browserist import Browser


def test_get_page_title(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.get.page_title() == "Example Domain"
