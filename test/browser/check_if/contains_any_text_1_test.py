import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, expected", [
    ("/html/body/div[5]/div[1]/div/h1", True),
    ("/html/body/div[5]/div[9]/div/div/div[3]/img", False),
    ("/does/not/exist", False),
])
def test_check_if_contains_any_text(xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.check_if.contains_any_text(xpath) is expected
