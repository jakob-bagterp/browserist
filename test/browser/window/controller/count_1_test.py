import pytest
from _mock_data.window_handles import WINDOW_HANDLE_1_ID, WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME

from browserist.model.window.controller import WindowHandleController


@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_add_handle(window_handle_controller: WindowHandleController) -> None:
    assert window_handle_controller.count() == 3
    window_handle_controller.add_handle(WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME)
    assert window_handle_controller.count() == 4
    window_handle_controller.remove_handle_by_id(WINDOW_HANDLE_1_ID)
    assert window_handle_controller.count() == 3
    window_handle_controller.remove_handle_by_name(WINDOW_HANDLE_2_NAME)
    assert window_handle_controller.count() == 2
