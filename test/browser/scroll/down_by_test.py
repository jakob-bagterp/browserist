import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("pixels", [
    1,
    100,
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_down_by(pixels: int, browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_top()
    browser.scroll.down_by(pixels)
    _, y_down = browser.scroll.get.position()
    assert y_down == pixels
