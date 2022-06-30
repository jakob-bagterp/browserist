import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("x, y", [
    (0, 50),
])
def test_scroll_by(x: int, y: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.page.to_top()
    browser.scroll.by(x, y)
    get_x, get_y = browser.scroll.get_position()
    assert get_x == x and get_y == y
