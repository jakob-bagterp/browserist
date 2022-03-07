import pytest

from browserist import helper


@pytest.mark.parametrize("id, expected", [
    ("Not valid ID", False),
    ("CDwindow-8088CB616D7499360039D98453AE91FC", True),
])
def test_helper_window_handle_is_valid_id(id: str, expected: bool) -> None:
    assert helper.window_handle.is_valid_id(id) is expected
