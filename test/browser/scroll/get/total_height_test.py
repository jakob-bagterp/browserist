import pytest
from _mock_data.url import internal_url

from browserist import Browser

MARGIN = 0.10  # 10%


@pytest.mark.parametrize("url, expected_total_scroll_height", [
    (internal_url.EXAMPLE_COM, 600),
    (internal_url.W3SCHOOLS_COM, 16465),
])
def test_get_total_scroll_height(url: str, expected_total_scroll_height: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    total_scroll_height = browser.scroll.get.total_height()
    # Various browsers may calculate the height differently, e.g. due to differient default widths, so we add a safety margin:
    minimum_height = expected_total_scroll_height - (expected_total_scroll_height * MARGIN)
    maximim_height = expected_total_scroll_height + (expected_total_scroll_height * MARGIN)
    assert minimum_height < total_scroll_height < maximim_height
