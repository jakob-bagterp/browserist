import pytest
from pytest import MonkeyPatch

from browserist import helper


@pytest.mark.parametrize("user_input, validate_input_regex", [("is_valid", "is_valid"), ("123456789", r"\d")])
def test_prompt_user_for_valid_value(
    user_input: str, validate_input_regex: str | None, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    output = helper.terminal.prompt_user_for_value("Input a value:", validate_input_regex)
    assert user_input == output


@pytest.mark.parametrize(
    "user_input_invalid, user_input_valid, validate_input_regex",
    [("is_not_valid", "is_valid", "is_valid"), ("is_not_valid", "123456789", r"\d")],
)
def test_prompt_user_for_invalid_value(
    user_input_invalid: str, user_input_valid: str, validate_input_regex: str | None, monkeypatch: MonkeyPatch
) -> None:
    """Test sequence invalid and valid user inputs."""

    inputs = iter([user_input_invalid, user_input_valid])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    output = helper.terminal.prompt_user_for_value("Input a value:", validate_input_regex)
    assert output == user_input_valid
