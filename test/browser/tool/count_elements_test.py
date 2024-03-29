import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_count", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p", 2),
    (internal_url.W3SCHOOLS_COM, "/html/body/div[5]/div[7]/div/div", 6),
    (internal_url.W3SCHOOLS_COM, "/html/body/div[5]/div[8]/div/div", 34),
])
def test_tool_count_elements(url: str, xpath: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.tool.count_elements(xpath) == expected_count
