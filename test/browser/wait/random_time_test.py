import time

import pytest

from browserist import Browser


@pytest.mark.parametrize("min_seconds, max_seconds", [
    (1, 2),
    (2, 4),
])
def test_wait_random_time(min_seconds: int, max_seconds: int, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    start_time_ns = time.perf_counter_ns()
    browser.wait.random_time(min_seconds, max_seconds)
    stop_time_ns = time.perf_counter_ns()
    elapsed_time_seconds = (stop_time_ns - start_time_ns) / 1_000_000_000
    assert min_seconds <= elapsed_time_seconds
    assert elapsed_time_seconds <= max_seconds
