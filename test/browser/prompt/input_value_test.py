import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from pytest import MonkeyPatch

from browserist import Browser

SEARCH_INPUT_XPATH = "//input[@id='search2']"


@pytest.mark.parametrize("user_input, validate_input_regex", [
    ("user input", r"."),
])
def test_prompt_input_value(user_input: str, validate_input_regex: str, browser_default_headless: Browser, monkeypatch: MonkeyPatch) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.get.attribute.value(SEARCH_INPUT_XPATH, "value") == ""
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    browser.prompt.input_value(SEARCH_INPUT_XPATH, "Input a value:", validate_input_regex)
    assert browser.get.attribute.value(SEARCH_INPUT_XPATH, "value") == user_input
