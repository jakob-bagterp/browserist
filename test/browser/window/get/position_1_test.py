from _helper.url import internal_url

from browserist import Browser


def test_window_get_position(browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    x_default, y_default = browser.window.get.position()
    x_new = x_default + 20
    y_new = y_default + 20
    browser.window.set.position(x_new, y_new)
    get_x, get_y = browser.window.get.position()
    assert get_x == x_new > x_default and get_y == y_new > y_default
