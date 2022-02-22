from _helper import internal_url

from browserist import Browser


def test_get_text_from_element(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.get.text.from_element("/html/body/div/p[2]") == "More information..."
