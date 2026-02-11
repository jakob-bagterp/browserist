import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_get_position(browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    x_default, y_default = browser.window.get.position()
    x_new = x_default + 20
    y_new = y_default + 20
    browser.window.set.position(x_new, y_new)
    get_x, get_y = browser.window.get.position()
    assert get_x == x_new > x_default
    assert get_y == y_new > y_default
