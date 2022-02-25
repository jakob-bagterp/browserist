from _helper import internal_url

from browserist import Browser


def test_window_minimize(browser_default: Browser) -> None:
    """Minizing the window doesn't change the size as it only hides the window."""

    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    default_width, default_height = browser.window.get.size()
    browser.window.minimize()
    minimized_width, minimized_height = browser.window.get.size()

    assert default_width == minimized_width
    assert default_height == minimized_height
