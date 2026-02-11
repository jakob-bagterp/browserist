import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("x, y", [
    (0, 50),
    (0, 200),
    (0, 100),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_by(x: int, y: int, browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_top()
    browser.scroll.by(x, y)
    x_get, y_get = browser.scroll.get.position()
    assert x_get == x
    assert y_get == y
