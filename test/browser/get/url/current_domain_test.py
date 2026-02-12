import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


@pytest.mark.parametrize(
    "url, expected_domain",
    [
        ("http://example.com/", "example.com"),
        ("http://www.example.com/", "www.example.com"),
        ("https://www.google.com/some/page", "www.google.com"),
    ],
)
def test_get_current_domain(url: str, expected_domain: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.current_domain() == expected_domain
