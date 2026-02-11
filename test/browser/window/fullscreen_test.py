import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_fullscreen(browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    default_width, default_height = browser.window.get.size()
    browser.window.fullscreen()
    fullscreen_width, fullscreen_height = browser.window.get.size()
    assert default_width <= fullscreen_width
    assert default_height <= fullscreen_height
