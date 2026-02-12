from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import (
    WINDOW_HANDLE_3_ID,
    WINDOW_HANDLE_3_NAME,
    WINDOW_HANDLE_4_ID,
    WINDOW_HANDLE_4_NAME,
    WINDOW_HANDLE_5_ID,
    WINDOW_HANDLE_5_NAME,
    WINDOW_HANDLE_6_ID,
    WINDOW_HANDLE_6_NAME,
)

from browserist.exception.window_handle import (
    WindowHandleIdNotUniqueError,
    WindowHandleIdNotValidError,
    WindowHandleNameNotUniqueError,
)
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize(
    "id, name, expected_handle_count",
    [
        (WINDOW_HANDLE_4_ID, None, 4),
        (WINDOW_HANDLE_5_ID, "random name", 4),
        (WINDOW_HANDLE_6_ID, WINDOW_HANDLE_6_NAME, 4),
    ],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_add_handle(
    id: str, name: str | None, expected_handle_count: int, window_handle_controller: WindowHandleController
) -> None:
    window_handle_controller.add_handle(id, name)
    assert len(window_handle_controller._window_handles) == expected_handle_count


@pytest.mark.parametrize(
    "id, name, expectation",
    [
        (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
        ("Not valid ID", WINDOW_HANDLE_5_NAME, pytest.raises(WindowHandleIdNotValidError)),
    ],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_add_handle_id_invalid_error(
    id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController
) -> None:
    with expectation:
        _ = window_handle_controller.add_handle(id, name) is not None


@pytest.mark.parametrize(
    "id, name, expectation",
    [
        (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
        (WINDOW_HANDLE_3_ID, WINDOW_HANDLE_5_NAME, pytest.raises(WindowHandleIdNotUniqueError)),
    ],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_add_handle_id_already_exist_error(
    id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController
) -> None:
    with expectation:
        _ = window_handle_controller.add_handle(id, name) is not None


@pytest.mark.parametrize(
    "id, name, expectation",
    [
        (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
        (WINDOW_HANDLE_5_ID, WINDOW_HANDLE_3_NAME, pytest.raises(WindowHandleNameNotUniqueError)),
    ],
)
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_handle_controller_add_handle_name_error(
    id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController
) -> None:
    with expectation:
        _ = window_handle_controller.add_handle(id, name) is not None
