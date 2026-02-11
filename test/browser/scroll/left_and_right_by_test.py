import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

RIGHT_BY_100_PIXELS: int = 100

LEFT_BY_20_PIXELS: int = 20

DIFFERENCE_BETWEEN_LEFT_AND_RIGHT: int = abs(RIGHT_BY_100_PIXELS - LEFT_BY_20_PIXELS)


@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_left_and_right_by(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.SCROLL_CANVAS)
    x_0, y_0 = browser.scroll.get.position()
    assert x_0 == y_0 == 0
    browser.scroll.right_by(RIGHT_BY_100_PIXELS)
    x_1, y_1 = browser.scroll.get.position()
    assert y_1 == y_0 == 0
    assert x_1 == RIGHT_BY_100_PIXELS
    browser.scroll.left_by(LEFT_BY_20_PIXELS)
    x_2, y_2 = browser.scroll.get.position()
    assert y_2 == y_1 == y_0 == 0
    assert x_2 == DIFFERENCE_BETWEEN_LEFT_AND_RIGHT
