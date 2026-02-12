import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected", [(internal_url.NOT_SCROLLABLE, True), (internal_url.SCROLL_LONG_VERTICAL, False)]
)
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_check_if_scroll_is_end_of_page_1(url: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    browser.scroll.page.to_top()
    assert browser.scroll.check_if.is_end_of_page() is expected


def test_check_if_scroll_is_end_of_page_2(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_end()
    browser.scroll.up_by(5)
    assert browser.scroll.check_if.is_end_of_page() is False
