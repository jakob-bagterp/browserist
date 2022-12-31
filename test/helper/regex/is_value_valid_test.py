import pytest

from browserist import helper


@pytest.mark.parametrize("value, regex, expected", [
    ("is_valid", "is_valid", True),
    ("is_valid", r"is_valid", True),
    ("123456789", r"\d", True),
    ("is_not_valid", "no_match_regex", False),
])
def test_is_value_valid(value: str, regex: str, expected: bool) -> None:
    assert helper.regex.is_value_valid(value, regex) is expected
