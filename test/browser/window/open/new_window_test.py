import pytest
from _config.browser_settings import default
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url1, url2", [
    (internal_url.MINI_SITE_HOMEPAGE, None),
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_FEATURE_1),
])
def test_open_new_window(url1: str, url2: str) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(url1)
        url_1 = browser.get.url.current()
        window_handle_1 = browser.window.handle.current()
        number_of_window_handles_1 = browser.window.handle.count(selenium=True)

        browser.window.open.new_window(url2)
        url_2 = browser.get.url.current()
        window_handle_2 = browser.window.handle.current()
        number_of_window_handles_2 = browser.window.handle.count(selenium=True)

        assert url_1 != url_2
        assert window_handle_1 != window_handle_2
        assert number_of_window_handles_1 != number_of_window_handles_2
        assert number_of_window_handles_1 == 1
        assert number_of_window_handles_2 == 2
