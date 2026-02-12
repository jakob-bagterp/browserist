import time

import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url, internal_url

from browserist import Browser

MAX_TIME_TO_OPEN_INTERNAL_PAGE = 10_000_000  # Nanoseconds.


@pytest.mark.parametrize(
    "url1, url2",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE),
        (internal_url.MINI_SITE_HOMEPAGE, external_url.EXAMPLE_COM),
        (internal_url.MINI_SITE_FEATURE_1, internal_url.MINI_SITE_FEATURE_1),
        (internal_url.MINI_SITE_FEATURE_1, external_url.EXAMPLE_COM),
    ],
)
def test_open_url_if_not_current_by_timing_performance(url1: str, url2: str, browser_default_headless: Browser) -> None:
    """Ensure that not re-opening an existing URL is more efficient than reloading the page.

    Tests the open.url_if_not_current() method indirectly by evaluating timing and network performance of differenc between opening an internal and external URL.

    Only run on a local machine. This test is likely to fail on GitHub Actions."""

    is_same_url = url1 == url2
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url1)
    time_start = time.perf_counter_ns()
    browser.open.url_if_not_current(url2)
    time_stop = time.perf_counter_ns()
    time_difference = _helper.time.get_difference(time_start, time_stop)
    if is_same_url:
        assert time_difference < MAX_TIME_TO_OPEN_INTERNAL_PAGE
    else:
        assert time_difference >= MAX_TIME_TO_OPEN_INTERNAL_PAGE
