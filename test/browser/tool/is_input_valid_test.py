import pytest
from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

@pytest.mark.parametrize("text, regex, ignore_case, expected", [
    ("test", r"test", False, True),
    ("test", r"TEST", False, False),
    ("test", r"tEsT", True, True),
    ("testing", r"test", False, False)
])
def test_tool_is_input_valid(text: str, regex: str, ignore_case: bool, expected: bool) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        assert browser.tool.is_input_valid(text, regex, ignore_case) is expected
