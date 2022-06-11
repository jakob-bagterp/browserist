import pytest

from browserist import helper


@pytest.mark.parametrize("total_time, interval, expected_retries", [
    (1, 0.25, 4),
    (1, 0.33, 3),
    (10, 0.50, 20),
])
def test_helper_calculate_number_of_retries(total_time: int, interval: float, expected_retries: int) -> None:
    assert helper.retry.calculate_number_of_retries(total_time, interval) == expected_retries
