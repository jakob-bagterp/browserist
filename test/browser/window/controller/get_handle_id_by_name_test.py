from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import (WINDOW_HANDLE_1_ID, WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_2_ID,
                                       WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_3_ID, WINDOW_HANDLE_3_NAME)

from browserist.exception.window_handle import WindowHandleNameNotFoundError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("name, expected", [
    (WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_1_ID),
    (WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_2_ID),
    (WINDOW_HANDLE_3_NAME, WINDOW_HANDLE_3_ID),
])
def test_window_handle_controller_get_handle_id_by_name(name: str, expected: str, window_handle_controller: WindowHandleController) -> None:
    assert window_handle_controller.get_handle_id_by_name(name) == expected


@pytest.mark.parametrize("name, expectation", [
    (WINDOW_HANDLE_1_NAME, does_not_raise()),
    ("Not valid name", pytest.raises(WindowHandleNameNotFoundError)),
])
def test_window_handle_controller_get_handle_id_by_name_not_found_error(name: str, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        window_handle_controller.get_handle_id_by_name(name) is not None
