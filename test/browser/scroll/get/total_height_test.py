import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_total_scroll_height",
    [(internal_url.NOT_SCROLLABLE, 600), (internal_url.SCROLL_LONG_VERTICAL, 40802)],
)
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_get_total_scroll_height(
    url: str, expected_total_scroll_height: int, browser_default_headless_scope_function: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(url)
    total_scroll_height = browser.scroll.get.total_height()
    # Various browsers may calculate the height differently, e.g. due to differient default widths, so we add a safety margin:
    minimum_height = _helper.tolerance.deduct_percent(expected_total_scroll_height, 50)
    maximum_height = _helper.tolerance.add_percent(expected_total_scroll_height, 50)
    assert minimum_height < total_scroll_height < maximum_height
