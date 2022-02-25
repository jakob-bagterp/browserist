from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForUrlTimeoutException


@pytest.mark.parametrize("url1, url2, url2_fragment, expectation", [
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM, "w3schools", does_not_raise()),
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM, internal_url.W3SCHOOLS_COM, does_not_raise()),
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM, "no_match", pytest.raises(WaitForUrlTimeoutException)),
])
def test_wait_until_url_contains(url1: str, url2: str, url2_fragment: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url1)
        browser.open.url(url2)
        browser.wait.until_url_contains(url2_fragment, timeout.VERY_SHORT) is not None
