from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import (WINDOW_HANDLE_3_NAME, WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME,
                                       WINDOW_HANDLE_5_ID, WINDOW_HANDLE_5_NAME, WINDOW_HANDLE_6_ID,
                                       WINDOW_HANDLE_6_NAME)

from browserist.exception.window_handle import WindowHandleIdNotValidError, WindowHandleNameNotUniqueError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("id, name, expected", [
    (WINDOW_HANDLE_4_ID, None, 4),
    (WINDOW_HANDLE_5_ID, "random name", 4),
    (WINDOW_HANDLE_6_ID, WINDOW_HANDLE_6_NAME, 4),
])
def test_window_handle_controller_add_handle(id: str, name: str | None, expected: int, window_handle_controller: WindowHandleController) -> None:
    window_handle_controller.add_handle(id, name)
    assert len(window_handle_controller._window_handles) == expected


@pytest.mark.parametrize("id, name, expectation", [
    (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
    ("Not valid ID", WINDOW_HANDLE_5_NAME, pytest.raises(WindowHandleIdNotValidError)),
])
def test_window_handle_controller_add_handle_id_error(id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        window_handle_controller.add_handle(id, name) is not None


@pytest.mark.parametrize("id, name, expectation", [
    (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
    (WINDOW_HANDLE_5_ID, WINDOW_HANDLE_3_NAME, pytest.raises(WindowHandleNameNotUniqueError)),
])
def test_window_handle_controller_add_handle_name_error(id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        window_handle_controller.add_handle(id, name) is not None
