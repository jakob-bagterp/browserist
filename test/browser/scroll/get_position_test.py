from _helper import internal_url

from browserist import Browser


def test_get_scroll_position(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    x_default, y_default = browser.scroll.get_position()
    browser.scroll.to_end_of_page()
    _, y_end = browser.scroll.get_position()
    assert x_default == 0 and y_default == 0 and y_default < y_end
