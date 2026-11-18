import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

START_POSITION_Y = 500


@pytest.mark.parametrize("pixels", [1, 100])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_up_by(pixels: int, browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.SCROLL_VERTICAL_LONG)
    browser.scroll.to_position(0, START_POSITION_Y)
    _, y_start = browser.scroll.get.position()
    assert y_start == START_POSITION_Y
    browser.scroll.up_by(pixels)
    _, y_up = browser.scroll.get.position()
    assert y_up == y_start - pixels
