from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("url, xpath, expectation", [
    (internal_url.W3SCHOOLS_COM, "//input[@id='search2']", does_not_raise()),
    (internal_url.W3SCHOOLS_COM, "//input[@id='search2']/div", pytest.raises(WaitForElementTimeoutException)),
])
def test_input_clear(url: str, xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url)
        browser.input.clear(xpath, timeout.VERY_SHORT)
