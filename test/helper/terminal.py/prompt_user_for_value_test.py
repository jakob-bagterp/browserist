import pytest
from pytest import MonkeyPatch

from browserist import helper


@pytest.mark.parametrize("user_input, validate_input_regex", [
    ("is_valid", "is_valid"),
    ("123456789", r"\d"),
])
def test_prompt_user_for_value(user_input: str, validate_input_regex: str | None, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    output = helper.terminal.prompt_user_for_value("Input a  value: ", validate_input_regex)
    assert user_input == output
