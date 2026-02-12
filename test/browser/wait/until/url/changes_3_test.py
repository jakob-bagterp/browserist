from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize(
    "url1, url2, expectation",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_FEATURE_1, does_not_raise()),
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, pytest.raises(RetryTimeoutException)),
    ],
)
def test_wait_until_url_changes(url1: str, url2: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url1)
        browser.open.url(url2)
        _ = browser.wait.until.url.changes(url1, timeout.VERY_SHORT) is not None
