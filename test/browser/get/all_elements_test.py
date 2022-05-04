import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_count", [
    (internal_url.EXAMPLE_COM, "//p", 2),
    (internal_url.W3SCHOOLS_COM, "//h1", 11),
])
def test_get_all_elements(url: str, xpath: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    elements = browser.get.all_elements(xpath)
    assert len(elements) == expected_count
