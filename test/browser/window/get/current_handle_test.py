from _helper import internal_url

from browserist import Browser


def test_window_get_current_handle(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.window.get.current_handle() is not None
