from _mock_data.window_handles import WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME

from browserist.model.window.controller import WindowHandleController


def test_window_handle_controller_add_handle(window_handle_controller: WindowHandleController) -> None:
    assert window_handle_controller.count() == 3
    window_handle_controller.add_handle(WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME)
    assert window_handle_controller.count() == 4
    # TODO: Also remove handle to count backwards
