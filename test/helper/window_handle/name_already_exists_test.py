import pytest
from _mock_data.window_handles import WINDOW_HANDLE_1_NAME, WINDOW_HANDLES

from browserist import helper


@pytest.mark.parametrize("name, expected", [("Name does not exist", False), (WINDOW_HANDLE_1_NAME, True)])
def test_helper_window_handle_name_already_exists(name: str, expected: bool) -> None:
    assert helper.window_handle.name_already_exists(name, WINDOW_HANDLES) is expected
