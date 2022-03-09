from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.window_handles import WINDOW_HANDLE_3_NAME, WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, WINDOW_HANDLE_5_ID

from browserist.exception.window_handle import WindowHandleNameNotUniqueError
from browserist.model.window.controller import WindowHandleController


@pytest.mark.parametrize("id, name, expectation", [
    (WINDOW_HANDLE_4_ID, WINDOW_HANDLE_4_NAME, does_not_raise()),
    (WINDOW_HANDLE_5_ID, WINDOW_HANDLE_3_NAME, pytest.raises(WindowHandleNameNotUniqueError)),
])
def test_window_handle_controller_add_handle(id: str, name: str | None, expectation: Any, window_handle_controller: WindowHandleController) -> None:
    with expectation:
        window_handle_controller.add_handle(id, name) is not None
