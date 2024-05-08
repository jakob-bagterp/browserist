import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

MARGIN = 0.12  # 12%


@pytest.mark.parametrize("url, expected_total_scroll_height", [
    (internal_url.NOT_SCROLLABLE, 600),
    (internal_url.W3SCHOOLS_COM, 16465),
])
def test_get_total_scroll_height(url: str, expected_total_scroll_height: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    total_scroll_height = browser.scroll.get.total_height()
    # Various browsers may calculate the height differently, e.g. due to differient default widths, so we add a safety margin:
    minimum_height = expected_total_scroll_height - (expected_total_scroll_height * MARGIN)
    maximim_height = expected_total_scroll_height + (expected_total_scroll_height * MARGIN)
    assert minimum_height < total_scroll_height < maximim_height
