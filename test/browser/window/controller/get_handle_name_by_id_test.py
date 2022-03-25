from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import (WINDOW_HANDLE_1_ID, WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_2_ID,
                                       WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_3_ID, WINDOW_HANDLE_3_NAME)

from browserist.exception.window_handle import WindowHandleIdNotFoundError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("id, expected", [
    (WINDOW_HANDLE_1_ID, WINDOW_HANDLE_1_NAME),
    (WINDOW_HANDLE_2_ID, WINDOW_HANDLE_2_NAME),
    (WINDOW_HANDLE_3_ID, WINDOW_HANDLE_3_NAME),
])
def test_window_handle_controller_get_handle_name_by_id(id: str, expected: str, window_handle_controller: WindowHandleController) -> None:
    assert window_handle_controller.get_handle_name_by_id(id) == expected


@pytest.mark.parametrize("id, expectation", [
    (WINDOW_HANDLE_1_ID, does_not_raise()),
    ("Not valid ID", pytest.raises(WindowHandleIdNotFoundError)),
])
def test_window_handle_controller_get_handle_name_by_id_not_found_error(id: str, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        window_handle_controller.get_handle_name_by_id(id) is not None
