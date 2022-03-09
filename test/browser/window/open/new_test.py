import pytest
from _config.browser_settings import default
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url1, url2", [
    (internal_url.EXAMPLE_COM, None),
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM),
])
def test_open_new_window(url1: str, url2: str) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(url1)
        url_1 = browser.get.url.current()
        window_handle_1 = browser.window.handle.current()
        number_of_window_handles_1 = browser.window.handle.count()

        browser.window.open.new(url2)
        url_2 = browser.get.url.current()
        window_handle_2 = browser.window.handle.current()
        number_of_window_handles_2 = browser.window.handle.count()

        assert url_1 != url_2
        assert window_handle_1 != window_handle_2
        assert number_of_window_handles_1 != number_of_window_handles_2
        assert number_of_window_handles_1 == 1
        assert number_of_window_handles_2 == 2
