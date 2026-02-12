import pytest
from _mock_data.window_handles import (
    WINDOW_HANDLE_1_ID,
    WINDOW_HANDLE_2_ID,
    WINDOW_HANDLE_3_ID,
    WINDOW_HANDLE_4_ID,
    WINDOW_HANDLE_5_ID,
    WINDOW_HANDLE_6_ID,
)

from browserist import helper


@pytest.mark.parametrize(
    "id, expected",
    [
        ("Not valid ID", False),
        (WINDOW_HANDLE_1_ID, True),
        (WINDOW_HANDLE_2_ID, True),
        (WINDOW_HANDLE_3_ID, True),
        (WINDOW_HANDLE_4_ID, True),
        (WINDOW_HANDLE_5_ID, True),
        (WINDOW_HANDLE_6_ID, True),
    ],
)
def test_helper_window_handle_is_valid_id(id: str, expected: bool) -> None:
    assert helper.window_handle.is_valid_id(id) is expected
