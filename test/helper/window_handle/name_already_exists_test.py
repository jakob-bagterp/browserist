import pytest
from _mock_data.window_handles import WINDOW_HANDLES

from browserist import helper


@pytest.mark.parametrize("name, expected", [
    ("Name does not exist", False),
    (WINDOW_HANDLES[0].name, True),
])
def test_helper_window_handle_name_already_exists(name: str, expected: bool) -> None:
    assert helper.window_handle.name_already_exists(name, WINDOW_HANDLES) is expected
