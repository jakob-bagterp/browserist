from _mock_data.url import internal_url

from browserist import Browser


def test_get_screen_width_non_headless(browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    screen_width = browser.screen.width()
    window_width, _ = browser.window.get.size()
    assert window_width >= screen_width > 0
