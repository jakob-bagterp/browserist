import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, tag, expected_count", [
    (internal_url.EXAMPLE_COM, "h1", 1),
    (internal_url.EXAMPLE_COM, "a", 1),
    (internal_url.W3SCHOOLS_COM, "h1", 11),
    (internal_url.W3SCHOOLS_COM, "h2", 48),
    (internal_url.W3SCHOOLS_COM, "a", 314),
])
def test_get_all_elements_by_tag(url: str, tag: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    elements = browser.get.all_elements_by_tag(tag)
    assert len(elements) == expected_count
