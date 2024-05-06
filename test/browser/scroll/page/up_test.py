import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper import operating_system


@pytest.mark.parametrize("pages", [
    1,
    2,
    3,
    4,
    5,
])
def test_scroll_page_up(pages: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_end()
    _, y_end = browser.scroll.get.position()
    y_screen_height = browser.viewport.get.height()
    browser.scroll.page.up(pages)
    _, y_page_up = browser.scroll.get.position()
    expected_exact_position = y_end - (y_screen_height - 1) * pages
    match _:  # Sometimes the scroll position is not calculated exactly on Windows nor macOS, and so we just do an approximation.
        case _ if operating_system.is_windows():
            assert y_page_up < y_end
        case _ if operating_system.is_mac_os():
            assert y_page_up <= _helper.tolerance.add(expected_exact_position, 10)
            assert y_page_up >= _helper.tolerance.deduct(expected_exact_position, 10)
        case _:
            assert y_page_up == expected_exact_position
