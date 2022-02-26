import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("width, height", [
    (500, 500),  # 500 is minimum width and height.
    (600, 600),
])
def test_window_get_size(width: int, height: int, browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.window.set.size(width, height)
    get_width, get_height = browser.window.get.size()
    assert width == get_width and height <= get_height
