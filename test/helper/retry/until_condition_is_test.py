from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, helper_iteration
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException

TRUE = "true"

FALSE = "false"


def return_bool(_: object, input: str) -> bool:
    return input == TRUE


@pytest.mark.parametrize(
    "input, expectation", [(FALSE, pytest.raises(RetryTimeoutException)), (TRUE, does_not_raise())]
)
def test_helper_retry_until_condition_is_true(input: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        _ = (
            helper_iteration.retry.until_condition_is_true(
                browser._browser_driver, input, func=return_bool, timeout=timeout.VERY_SHORT
            )
            is not None
        )


@pytest.mark.parametrize(
    "input, expectation", [(FALSE, does_not_raise()), (TRUE, pytest.raises(RetryTimeoutException))]
)
def test_helper_retry_until_condition_is_false(input: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        _ = (
            helper_iteration.retry.until_condition_is_false(
                browser._browser_driver, input, func=return_bool, timeout=timeout.VERY_SHORT
            )
            is not None
        )
