import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected", [
    (internal_url.EXAMPLE_COM, "Example Domain"),
    (internal_url.W3SCHOOLS_COM, "W3Schools Online Web Tutorials"),
])
def test_get_page_title(url: str, expected: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.page_title() == expected
