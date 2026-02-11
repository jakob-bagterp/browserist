import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected_total_scroll_width", [
    (internal_url.NOT_SCROLLABLE, 900),
    (internal_url.SCROLL_WIDE_HORIZONTAL, 10000),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_get_total_scroll_width(url: str, expected_total_scroll_width: int, browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(url)
    total_scroll_width = browser.scroll.get.total_width()
    # Various browsers may calculate the width differently, e.g. due to differient default widths, so we add a safety margin:
    minimum_width = _helper.tolerance.deduct(expected_total_scroll_width, 50)
    maximum_width = _helper.tolerance.add(expected_total_scroll_width, 50)
    assert minimum_width < total_scroll_width < maximum_width
