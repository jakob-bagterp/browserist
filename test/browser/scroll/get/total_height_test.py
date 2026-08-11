import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper import operating_system


@pytest.mark.parametrize(
    "url, expected_total_scroll_height, tolerance_pixels",
    [
        (internal_url.NOT_SCROLLABLE, 437, 10),
        (internal_url.SCROLL_VERTICAL_LONG, 42_076, 1_000 if operating_system.is_windows() else 400),
    ],
)
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_get_total_scroll_height(
    url: str, expected_total_scroll_height: int, tolerance_pixels: int, browser_default_headless_scope_function: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(url)
    total_scroll_height = browser.scroll.get.total_height()
    minimum_height = expected_total_scroll_height - tolerance_pixels
    assert minimum_height < total_scroll_height
    maximum_height = expected_total_scroll_height + tolerance_pixels
    assert total_scroll_height < maximum_height
