import pytest

from browserist import Browser


@pytest.mark.parametrize("url, expected", [
    ("http://example.com/", "http://example.com/"),
    ("http://example.com", "http://example.com/"),
])
def test_get_current_url(url: str, expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url_if_not_current(url)
    assert browser.get.url.current() == expected
