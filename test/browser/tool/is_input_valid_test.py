import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "text, regex, ignore_case, expected",
    [
        ("test", r"test", False, True),
        ("test", r"TEST", False, False),
        ("test", r"tEsT", True, True),
        ("testing", r"test", False, False),
    ],
)
def test_tool_is_input_valid(
    text: str, regex: str, ignore_case: bool, expected: bool, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    assert browser.tool.is_input_valid(text, regex, ignore_case) is expected
