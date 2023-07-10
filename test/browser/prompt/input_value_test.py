import pytest
from _constant.string import EMPTY_STRING
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath import xpath
from pytest import MonkeyPatch

from browserist import Browser


@pytest.mark.parametrize("user_input, validate_input_regex", [
    ("user input", r"."),
])
def test_prompt_input_value(user_input: str, validate_input_regex: str, browser_default_headless: Browser, monkeypatch: MonkeyPatch) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.get.attribute.value(xpath.W3SchoolsCom.SEARCH_INPUT, "value") == EMPTY_STRING
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    browser.prompt.input_value(xpath.W3SchoolsCom.SEARCH_INPUT, "Input a value:", validate_input_regex)
    assert browser.get.attribute.value(xpath.W3SchoolsCom.SEARCH_INPUT, "value") == user_input
