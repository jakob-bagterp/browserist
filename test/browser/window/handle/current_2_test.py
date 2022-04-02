from _mock_data.url import internal_url

from browserist import Browser


def test_get_current_window_handle(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.window.handle.current() is not None
