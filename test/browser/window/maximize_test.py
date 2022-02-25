from _helper import internal_url

from browserist import Browser


def test_window_maximize(browser_default: Browser) -> None:
    """This test may fail if tested on a multiple screen setup."""

    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    default_width, default_height = browser.window.get.size()
    browser.window.maximize()
    maximized_width, maximized_height = browser.window.get.size()

    assert default_width <= maximized_width
    assert default_height <= maximized_height
