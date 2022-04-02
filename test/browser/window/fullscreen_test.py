from _mock_data.url import internal_url

from browserist import Browser


def test_window_fullscreen(browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    default_width, default_height = browser.window.get.size()
    browser.window.fullscreen()
    fullscreen_width, fullscreen_height = browser.window.get.size()
    assert default_width <= fullscreen_width and default_height <= fullscreen_height
