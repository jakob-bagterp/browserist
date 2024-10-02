import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url", [
    (internal_url.MINI_SITE_HOMEPAGE),
    (internal_url.MINI_SITE_FEATURE_1),
    (internal_url.MINI_SITE_ABOUT),
])
def test_get_page_source(url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    loaded_page_source = browser.get.page_source()
    url_as_file_path = _helper.url.convert_internal_url_to_file_path(url)
    with open(url_as_file_path) as file:
        expected_page_source = file.read()
    assert loaded_page_source == expected_page_source
