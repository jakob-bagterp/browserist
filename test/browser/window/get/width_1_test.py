import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width, height", [
    (520, 520),  # 500 is minimum width and height for Chrome, 513 on Edge.
    (600, 600),
])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_get_width(width: int, height: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.size(width, height)
    get_width = browser.window.get.width()
    assert width <= get_width
