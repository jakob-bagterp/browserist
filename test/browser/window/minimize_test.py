import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_minimize(browser_default: Browser) -> None:
    """Minizing the window doesn't change the size as it only hides the window."""

    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.size(520, 520)  # 500 is minimum width and height for Chrome, 513 on Edge.
    default_width, default_height = browser.window.get.size()
    browser.window.minimize()
    minimized_width, minimized_height = browser.window.get.size()
    assert default_width == minimized_width
    assert default_height == minimized_height
