import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected_title", [
    (internal_url.EXAMPLE_COM, "Example Domain"),
    (internal_url.W3SCHOOLS_COM, "W3Schools Online Web Tutorials"),
])
def test_get_page_title(url: str, expected_title: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.page_title() == expected_title
