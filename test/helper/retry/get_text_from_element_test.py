from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, helper_iteration
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


def return_input(_: object, input: str) -> str:
    return input


@pytest.mark.parametrize("input, expectation", [("text", does_not_raise()), ("", pytest.raises(RetryTimeoutException))])
def test_helper_retry_get_text(input: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        _ = (
            helper_iteration.retry.get_text(browser._browser_driver, input, return_input, timeout.VERY_SHORT)
            is not None
        )
