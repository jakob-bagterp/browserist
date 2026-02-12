from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForWindowTimeoutException


@pytest.mark.parametrize(
    "open_new_tabs, open_new_windows, expected_handles, expected_exception",
    [
        (1, 1, 3, does_not_raise()),
        (0, 1, 2, does_not_raise()),
        (1, 0, 2, does_not_raise()),
        (1, 1, 1, pytest.raises(WaitForWindowTimeoutException)),
        (0, 1, 1, pytest.raises(WaitForWindowTimeoutException)),
        (1, 0, 1, pytest.raises(WaitForWindowTimeoutException)),
        (0, 0, -1, pytest.raises(ValueError)),
    ],
)
def test_wait_until_number_of_window_handles_is(
    open_new_tabs: int,
    open_new_windows: int,
    expected_handles: int,
    expected_exception: Any,
    browser_default_headless_scope_function: Browser,
) -> None:
    """As the browser already has one tab open by default, we test the number of new windows or tabs plus 1."""

    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    with expected_exception:
        for _ in range(open_new_tabs):
            browser.window.open.new_tab()
        for _ in range(open_new_windows):
            browser.window.open.new_window()
        _ = browser.wait.until.number_of_window_handles_is(expected_handles, timeout.VERY_SHORT) is not None
