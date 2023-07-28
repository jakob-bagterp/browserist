import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected", [
    (internal_url.EXAMPLE_COM, True),  # Doesn't allow for scrolling.
    (internal_url.W3SCHOOLS_COM, False),  # Long page that allows for scrolling.
])
def test_check_if_scroll_is_end_of_page_1(url: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    browser.scroll.page.to_top()
    assert browser.scroll.check_if.is_end_of_page() is expected


def test_check_if_scroll_is_end_of_page_2(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    # Let's scroll all the way to the bottom of the page:
    browser.scroll.page.to_end()
    assert browser.scroll.check_if.is_end_of_page() is True
    # Now scroll a little up:
    browser.scroll.up_by(2)
    assert browser.scroll.check_if.is_end_of_page() is False
