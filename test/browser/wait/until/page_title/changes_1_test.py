from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("baseline_text, expectation", [
    ("Not the current page title", does_not_raise()),
    ("Example Domain", pytest.raises(RetryTimeoutException)),
])
def test_wait_until_text_changes(baseline_text: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(internal_url.EXAMPLE_COM)
        browser.wait.until.page_title.changes(baseline_text, timeout.VERY_SHORT) is not None
