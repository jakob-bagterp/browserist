import pytest
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("xpath, regex, ignore_case, expected", [
    ("//*[@id='main']/div[1]/div/h1", "Learn to Code", False, True),
    ("//*[@id='main']/div[1]/div/h1", "code", False, False),
    ("//*[@id='main']/div[1]/div/h1", r"^learn", True, True),
    ("//*[@id='main']/div[1]/div/h1", r"^learn", False, False),
    ("/does/not/exist", "does not matter", True, False),
])
def test_check_if_contains_text(xpath: str, regex: str, ignore_case: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.check_if.contains_text(xpath, regex, ignore_case) is expected
