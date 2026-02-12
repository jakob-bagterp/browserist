import time

import pytest
from _constant.time import NANOSECONDS_PER_SECOND
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser

TIMING_MARGIN = 20 / 100  # 20%


@pytest.mark.parametrize("seconds", [1, 5.5])
def test_wait_seconds(seconds: float, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    start_time_ns = time.perf_counter_ns()
    browser.wait.seconds(seconds)
    stop_time_ns = time.perf_counter_ns()
    elapsed_time_seconds = (stop_time_ns - start_time_ns) / NANOSECONDS_PER_SECOND
    max_timing_margin_seconds = seconds + seconds * TIMING_MARGIN
    assert seconds <= elapsed_time_seconds
    assert elapsed_time_seconds <= max_timing_margin_seconds
