import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_text", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]", "More information..."),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a[1]", "Try Frontend Editor (HTML/CSS/JS)"),
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/h1", "W3Schools Spaces"),
])
def test_get_text(url: str, xpath: str, expected_text: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.text(xpath) == expected_text
