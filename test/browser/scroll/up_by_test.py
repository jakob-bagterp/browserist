import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("pixels", [
    1,
    100,
])
def test_scroll_up_by(pixels: int, browser_default_headless_scope_function: Browser) -> None:
    browser = browser_default_headless_scope_function
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.page.to_end()
    _, y_end = browser.scroll.get.position()
    browser.scroll.up_by(pixels)
    _, y_up = browser.scroll.get.position()
    assert y_end == y_up + pixels
