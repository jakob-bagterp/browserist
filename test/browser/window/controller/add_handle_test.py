import pytest
from _mock_data.window_handles import WINDOW_HANDLE_4_ID, WINDOW_HANDLE_5_ID, WINDOW_HANDLE_5_NAME

from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("id, name, expected", [
    (WINDOW_HANDLE_4_ID, None, 4),
    (WINDOW_HANDLE_5_ID, WINDOW_HANDLE_5_NAME, 5),
])
def test_window_handle_controller_add_handle(id: str, name: str | None, expected: int, window_handle_controller: WindowHandleController) -> None:
    window_handle_controller.add_handle(id, name)
    assert len(window_handle_controller._window_handles) == expected
