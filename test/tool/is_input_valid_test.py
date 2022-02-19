from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

def with_browser_tool_is_input_valid(text: str, regex: str, ignore_case: bool) -> bool:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        return browser.tool.is_input_valid(text, regex, ignore_case)

def test_tool_is_input_valid_1() -> None:
    assert with_browser_tool_is_input_valid("test", r"test", ignore_case = False) is True

def test_tool_is_input_valid_2() -> None:
    assert with_browser_tool_is_input_valid("test", r"TEST", ignore_case = False) is False

def test_tool_is_input_valid_3() -> None:
    assert with_browser_tool_is_input_valid("test", r"tEsT", ignore_case = True) is True

def test_tool_is_input_valid_4() -> None:
    assert with_browser_tool_is_input_valid("testing", r"test", ignore_case = False) is False
