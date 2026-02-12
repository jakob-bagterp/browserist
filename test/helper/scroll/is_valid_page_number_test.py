import pytest

from browserist.helper.scroll import is_valid_page_number


@pytest.mark.parametrize(
    "page_number, expected", [(1, True), (10, True), (0, False), (-5, False), (3.14, False), ("2", False)]
)
def test_is_valid_page_number(page_number: int, expected: bool) -> None:
    assert is_valid_page_number(page_number) is expected
