import pytest
from _config.browser_settings import default
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url1, url2",
    [(internal_url.MINI_SITE_HOMEPAGE, None), (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_FEATURE_1)],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_open_new_tab_in_window(url1: str, url2: str) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(url1)
        url_1 = browser.get.url.current()
        tab_handle_1 = browser.window.handle.current()
        number_of_tab_handles_1 = browser.window.handle.count(selenium=True)

        browser.window.open.new_tab(url2)
        url_2 = browser.get.url.current()
        tab_handle_2 = browser.window.handle.current()
        number_of_tab_handles_2 = browser.window.handle.count(selenium=True)

        assert url_1 != url_2
        assert tab_handle_1 != tab_handle_2
        assert number_of_tab_handles_1 != number_of_tab_handles_2
        assert number_of_tab_handles_1 == 1
        assert number_of_tab_handles_2 == 2
