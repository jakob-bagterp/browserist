from _helper import internal_url

from browserist import Browser


def test_scroll_to_top_of_page(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.to_end_of_page()
    x_end, y_end = browser.scroll.get_position()
    browser.scroll.to_top_of_page()
    x_top, y_top = browser.scroll.get_position()
    assert x_top == x_end == 0 and y_top < y_end
