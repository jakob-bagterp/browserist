import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected", [
    (internal_url.EXAMPLE_COM, True),  # Doesn't allow for scrolling.
    (internal_url.W3SCHOOLS_COM, False),  # Long page that allows for scrolling.
])
def test_check_if_scroll_is_end_of_page(url: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    browser.scroll.page.to_top()
    assert browser.scroll.check_if.is_end_of_page() is expected
