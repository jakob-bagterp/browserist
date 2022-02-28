import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("x, y", [
    (0, 0),
    (0, 200),
    (0, 100),
])
def test_scroll_to_position(x: int, y: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.to_position(x, y)
    get_x, get_y = browser.scroll.get_position()
    assert get_x == x and get_y == y
