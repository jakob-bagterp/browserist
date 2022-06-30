from _mock_data.url import internal_url

from browserist import Browser


def test_get_scroll_position(browser_default_headless_scope_function: Browser) -> None:
    browser = browser_default_headless_scope_function
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.page.to_top()
    x_default, y_default = browser.scroll.get_position()
    browser.scroll.page.to_end()
    _, y_end = browser.scroll.get_position()
    assert x_default == 0 and y_default == 0 and y_default < y_end
