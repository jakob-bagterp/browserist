from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url

from browserist import Browser
from browserist import helper
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


def always_false() -> bool:
    return False


def always_true() -> bool:
    return True


@pytest.mark.parametrize("func, expectation", [
    (always_false(), pytest.raises(RetryTimeoutException)),
    (always_true(), does_not_raise()),
])
def test_helper_retry_until_condition_is_true(func: Any, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    with expectation:
        helper.retry.until_condition_is_true(func, timeout.VERY_SHORT) is not None


@pytest.mark.parametrize("func, expectation", [
    (always_false(), does_not_raise()),
    (always_true(), pytest.raises(RetryTimeoutException)),
])
def test_helper_retry_until_condition_is_false(func: Any, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    with expectation:
        helper.retry.until_condition_is_false(func, timeout.VERY_SHORT) is not None
