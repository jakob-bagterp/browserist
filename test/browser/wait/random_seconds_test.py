import time

import pytest
from _constant.time import NANOSECONDS_PER_SECOND
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


@pytest.mark.parametrize("min_seconds, max_seconds", [(1, 2), (2, 4)])
def test_wait_random_seconds(min_seconds: int, max_seconds: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    start_time_ns = time.perf_counter_ns()
    browser.wait.random_seconds(min_seconds, max_seconds)
    stop_time_ns = time.perf_counter_ns()
    elapsed_time_seconds = (stop_time_ns - start_time_ns) / NANOSECONDS_PER_SECOND
    assert min_seconds <= elapsed_time_seconds
    assert elapsed_time_seconds <= max_seconds
