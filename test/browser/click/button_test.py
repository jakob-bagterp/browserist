import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url, internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_url", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", external_url.IANA_ORG_EXAMPLE_DOMAINS),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a[1]",
     "https://www.w3schools.com/html/default.asp"),
])
def test_click_button(url: str, xpath: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    browser.click.button(xpath)
    browser.wait.until.url.contains(expected_url)
    assert browser.get.url.current() == expected_url
