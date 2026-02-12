import pytest

from browserist import helper


@pytest.mark.parametrize("size_to_be, size_current, expected_size", [(100, 100, 100), (200, 206, 194), (100, 92, 108)])
def test_helper_viewport_calculate_size_adjustment(size_to_be: int, size_current: int, expected_size: int) -> None:
    assert helper.viewport.calculate_size_adjustment(size_to_be, size_current) == expected_size
