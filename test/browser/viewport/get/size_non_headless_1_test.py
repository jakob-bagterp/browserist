import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.xdist_group(name="serial_viewport_tests")
def test_get_viewport_non_headless(browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    screen_width, screen_height = browser.viewport.get.size()
    window_width, window_height = browser.window.get.size()
    assert window_width >= screen_width > 0
    assert window_height > screen_height > 0
