import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("x1, y1, x2, y2", [(0, 0, 30, 60), (10, 30, 0, 70)])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_set_position(x1: int, y1: int, x2: int, y2: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.position(x1, y1)
    browser.window.set.position(x2, y2)
    get_x, get_y = browser.window.get.position()
    assert get_x == x2 != x1
    assert get_y == y2 != y1
