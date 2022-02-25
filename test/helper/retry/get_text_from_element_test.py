from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from browserist import helper
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


def always_has_text() -> str:
    return "text"


def always_has_no_text() -> str:
    return ""


@pytest.mark.parametrize("func, expectation", [
    (always_has_text(), does_not_raise()),
    (always_has_no_text(), pytest.raises(RetryTimeoutException)),
])
def test_helper_retry_get_text_from_element(func: Any, expectation: Any) -> None:
    with expectation:
        helper.retry.get_text_from_element(func, timeout.VERY_SHORT) is not None
