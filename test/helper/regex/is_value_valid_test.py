import pytest

from browserist import helper


@pytest.mark.parametrize(
    "value, regex, expected",
    [
        ("is valid", "is valid", True),
        ("is valid", r"is valid", True),
        ("123456789", r"\d", True),
        ("is not valid", "no match regex", False),
    ],
)
def test_is_value_valid(value: str, regex: str, expected: bool) -> None:
    assert helper.regex.is_value_valid(value, regex) is expected
