from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_4_NAME

from browserist.exception.window_handle import WindowHandleNameNotFoundError, WindowHandleNameNotValidError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("name", [
    (WINDOW_HANDLE_2_NAME),
])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_name(name: str, window_handle_controller: WindowHandleController) -> None:
    assert window_handle_controller.count() == 3
    window_handle_controller.remove_handle_by_name(name)
    assert window_handle_controller.count() == 2


@pytest.mark.parametrize("name, expectation", [
    (WINDOW_HANDLE_2_NAME, does_not_raise()),
    # This name is reserved for the original window:
    (WINDOW_HANDLE_1_NAME, pytest.raises(WindowHandleNameNotValidError)),
])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_name_invalid_error(name: str, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        _ = window_handle_controller.remove_handle_by_name(name) is not None


@pytest.mark.parametrize("name, expectation", [
    (WINDOW_HANDLE_2_NAME, does_not_raise()),
    (WINDOW_HANDLE_4_NAME, pytest.raises(WindowHandleNameNotFoundError)),
])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_remove_handle_by_name_not_found_error(name: str, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        _ = window_handle_controller.remove_handle_by_name(name) is not None
