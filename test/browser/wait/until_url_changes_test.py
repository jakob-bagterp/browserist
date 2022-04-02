from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("url1, url2, expectation", [
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM, does_not_raise()),
    (internal_url.EXAMPLE_COM, internal_url.EXAMPLE_COM, pytest.raises(RetryTimeoutException)),
])
def test_wait_until_url_changes(url1: str, url2: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url1)
        browser.open.url(url2)
        browser.wait.until_url_changes(url1, timeout.VERY_SHORT) is not None
