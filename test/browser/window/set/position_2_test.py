import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("x1, y1, x2, y2", [
    (0, 0, 30, 60),
    (10, 30, 0, 70),
])
def test_window_set_position(x1: int, y1: int, x2: int, y2: int, browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.window.set.position(x1, y1)
    browser.window.set.position(x2, y2)
    get_x, get_y = browser.window.get.position()
    assert get_x == x2 != x1 and get_y == y2 != y1
