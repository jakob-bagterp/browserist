import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div/p[2]/a", False),
    ("/html/body/div/h1/div", True),  # Element doesn't exist.
])
def test_check_if_is_disabled(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.check_if.is_disabled(xpath) is expected
