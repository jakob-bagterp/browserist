from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_get_screen_height_non_headless(browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.EXAMPLE_COM)
    screen_height = browser.screen.height()
    _, window_height = browser.window.get.size()
    assert window_height > screen_height > 0
