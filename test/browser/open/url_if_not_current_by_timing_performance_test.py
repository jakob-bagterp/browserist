import time

import pytest
from _helper.url import external_url, internal_url

from browserist import Browser

_max_time_to_open_internal_page = 10 * 1000 * 1000  # Nanoseconds.


@pytest.mark.parametrize("url1, url2", [
    (internal_url.EXAMPLE_COM, internal_url.EXAMPLE_COM),
    (internal_url.EXAMPLE_COM, external_url.EXAMPLE_COM),
    (internal_url.W3SCHOOLS_COM, internal_url.W3SCHOOLS_COM),
    (internal_url.W3SCHOOLS_COM, external_url.W3SCHOOLS_COM),
])
def test_open_url_if_not_current_by_timing_performance_test(url1: str, url2: str, browser_default_headless: Browser) -> None:
    """Ensure that not re-opening an existing URL is more efficient than reloading the pate.
    Tests the open.url_if_not_current() method indirectly by evaluating timing and network performance of differenc between opening an internal and external URL.

    This test is likely to fail, especially on GitHub Actions. Only run on a local machine."""

    is_same_url = url1 == url2
    browser = browser_default_headless
    browser.open.url(url1)
    time_start = time.perf_counter_ns()
    browser.open.url_if_not_current(url2)
    time_stop = time.perf_counter_ns()
    time_difference = time_stop - time_start
    if is_same_url:
        assert time_difference < _max_time_to_open_internal_page
    else:
        assert time_difference >= _max_time_to_open_internal_page
