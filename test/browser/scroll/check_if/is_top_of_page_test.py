import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, y_position, expected", [
    (internal_url.W3SCHOOLS_COM, 0, True),
    (internal_url.W3SCHOOLS_COM, 1, False),
    (internal_url.W3SCHOOLS_COM, 20, False),
])
def test_check_if_scroll_is_top_of_page(url: str, y_position: int, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    browser.scroll.to_position(0, y_position)
    assert browser.scroll.check_if.is_top_of_page() is expected
