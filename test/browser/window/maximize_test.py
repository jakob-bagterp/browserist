import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_maximize(browser_default: Browser) -> None:
    """This test may fail if tested on a multiple screens setup."""

    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.size(1, 1)
    default_width, default_height = browser.window.get.size()
    browser.window.maximize()
    maximized_width, maximized_height = browser.window.get.size()
    assert default_width <= maximized_width
    assert default_height <= maximized_height
