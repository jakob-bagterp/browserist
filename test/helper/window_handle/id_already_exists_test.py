import pytest
from _mock_data.window_handles import WINDOW_HANDLE_1_ID, WINDOW_HANDLES

from browserist import helper


@pytest.mark.parametrize("id, expected", [("ID does not exist", False), (WINDOW_HANDLE_1_ID, True)])
def test_helper_window_handle_id_already_exists(id: str, expected: bool) -> None:
    assert helper.window_handle.id_already_exists(id, WINDOW_HANDLES) is expected
