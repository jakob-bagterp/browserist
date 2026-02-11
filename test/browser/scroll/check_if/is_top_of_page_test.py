import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, y_position, expected", [
    (internal_url.SCROLL_LONG_VERTICAL, 0, True),
    (internal_url.SCROLL_LONG_VERTICAL, 1, False),
    (internal_url.SCROLL_LONG_VERTICAL, 20, False),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_check_if_scroll_is_top_of_page(url: str, y_position: int, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    browser.scroll.page.to_top()
    browser.scroll.to_position(0, y_position)
    assert browser.scroll.check_if.is_top_of_page() is expected
