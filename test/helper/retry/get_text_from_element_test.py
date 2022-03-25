from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from browserist import Browser, helper
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


def return_input(_: object, input: str) -> str:
    return input


@pytest.mark.parametrize("input, expectation", [
    ("text", does_not_raise()),
    ("", pytest.raises(RetryTimeoutException)),
])
def test_helper_retry_get_text_from_element(input: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        _ = helper.retry.get_text_from_element(browser.driver, input, return_input, timeout.VERY_SHORT) is not None
