import pytest
from _constant.string import EMPTY_STRING
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.contact import MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH
from pytest import MonkeyPatch

from browserist import Browser


@pytest.mark.parametrize("user_input, validate_input_regex", [("user input", r".")])
def test_prompt_input_value(
    user_input: str, validate_input_regex: str, browser_default_headless: Browser, monkeypatch: MonkeyPatch
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_CONTACT)
    assert browser.get.attribute.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "value") == EMPTY_STRING
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    browser.prompt.input_value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "Input a value:", validate_input_regex)
    assert browser.get.attribute.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "value") == user_input
