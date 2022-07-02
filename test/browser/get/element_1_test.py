import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected", [
    (internal_url.EXAMPLE_COM, "/html/body/div/h1", True),
    (internal_url.W3SCHOOLS_COM, "/html/body/div[5]/div[1]/div/h1", True),
])
def test_get_element(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert bool(browser.get.element(xpath)) is expected
