import pytest

from browserist import Browser


@pytest.mark.parametrize("url, expected_url", [
    ("http://example.com/", "http://example.com/"),
    ("http://example.com", "http://example.com/"),
])
def test_get_current_url(url: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.current() == expected_url
