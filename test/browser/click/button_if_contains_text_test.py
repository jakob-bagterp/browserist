import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url, internal_url

from browserist import Browser


@pytest.mark.parametrize("text, ignore_case", [
    ("More information", False),
    ("mOrE iNforMatiOn", True),
])
def test_click_button_if_contains_text(text: str, ignore_case: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.click.button_if_contains_text("/html/body/div/p[2]/a", text, ignore_case)
    browser.wait.until.url.contains(external_url.IANA_ORG_RESERVED_DOMAINS)
    assert browser.get.url.current() == external_url.IANA_ORG_RESERVED_DOMAINS
