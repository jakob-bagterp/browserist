from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import WINDOW_HANDLE_1_ID, WINDOW_HANDLE_4_ID

from browserist.exception.window_handle import WindowHandleIdNotFoundError, WindowHandleIdNotValidError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("id", [(WINDOW_HANDLE_1_ID)])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_id(
    id: str, window_handle_controller: WindowHandleController
) -> None:
    assert window_handle_controller.count() == 3
    window_handle_controller.remove_handle_by_id(id)
    assert window_handle_controller.count() == 2


@pytest.mark.parametrize(
    "id, expectation",
    [(WINDOW_HANDLE_1_ID, does_not_raise()), ("Not valid ID", pytest.raises(WindowHandleIdNotValidError))],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_id_invalid_error(
    id: str, expectation: Any, window_handle_controller: WindowHandleController
) -> None:
    with expectation:
        _ = window_handle_controller.remove_handle_by_id(id) is not None


@pytest.mark.parametrize(
    "id, expectation",
    [(WINDOW_HANDLE_1_ID, does_not_raise()), (WINDOW_HANDLE_4_ID, pytest.raises(WindowHandleIdNotFoundError))],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_id_not_found_error(
    id: str, expectation: Any, window_handle_controller: WindowHandleController
) -> None:
    with expectation:
        _ = window_handle_controller.remove_handle_by_id(id) is not None
