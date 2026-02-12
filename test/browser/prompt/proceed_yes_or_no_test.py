import pytest
from _helper.timeout import reset_to_not_timed_out
from pytest import MonkeyPatch

from browserist import Browser


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("", True),  # Simulates just pressing enter/return.
        ("y", True),
        ("yes", True),
        ("n", False),
        ("no", False),
    ],
)
def test_prompt_proceed_yes_or_no(
    user_input: str, expected: bool, browser_default_headless: Browser, monkeypatch: MonkeyPatch
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    assert browser.prompt.proceed_yes_or_no() is expected
