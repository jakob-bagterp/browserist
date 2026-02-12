import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_url",
    [("https://example.com/", "https://example.com/"), ("https://example.com", "https://example.com/")],
)
def test_get_current_url(url: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.current() == expected_url
