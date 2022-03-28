import pytest
from _helper.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("text, regex, ignore_case, expected", [
    ("test", r"test", False, True),
    ("test", r"TEST", False, False),
    ("test", r"tEsT", True, True),
    ("testing", r"test", False, False),
])
def test_tool_is_input_valid(text: str, regex: str, ignore_case: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.tool.is_input_valid(text, regex, ignore_case) is expected
