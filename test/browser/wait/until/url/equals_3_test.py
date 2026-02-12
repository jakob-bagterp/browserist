from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForUrlTimeoutException


@pytest.mark.parametrize(
    "url1, url2, expectation",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, does_not_raise()),
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_FEATURE_1, pytest.raises(WaitForUrlTimeoutException)),
    ],
)
def test_wait_until_url_equals(url1: str, url2: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url1)
        browser.open.url(url2)
        _ = browser.wait.until.url.equals(url1, timeout.VERY_SHORT) is not None
