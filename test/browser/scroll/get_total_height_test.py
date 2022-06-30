import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected_total_scroll_height", [
    (internal_url.EXAMPLE_COM, 600),
    (internal_url.W3SCHOOLS_COM, 16465),
])
def test_get_total_scroll_height(url: str, expected_total_scroll_height: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    total_scroll_height = browser.scroll.get_total_height()
    assert total_scroll_height == expected_total_scroll_height
