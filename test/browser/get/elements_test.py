import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_count", [
    (internal_url.EXAMPLE_COM, "//p", 2),
    (internal_url.W3SCHOOLS_COM, "//h1", 11),
])
def test_get_elements(url: str, xpath: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    elements = browser.get.elements(xpath)
    assert len(elements) == expected_count
