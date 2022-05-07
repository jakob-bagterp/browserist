import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_width, expected_height", [
    (internal_url.EXAMPLE_COM, "/html/body/div", 600, 167),
    (internal_url.EXAMPLE_COM, "/html/body/div/h1", 600, 38),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[7]/div/div[1]", 444, 265),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[8]/div/div[1]", 192, 113),
])
def test_get_dimensions(url: str, xpath: str, expected_width: int, expected_height: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert expected_width, expected_height == browser.get.dimensions(xpath)
