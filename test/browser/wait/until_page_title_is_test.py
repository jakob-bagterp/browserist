from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForPageTitleToChangeTimeoutException


@pytest.mark.parametrize("url, page_title, expectation", [
    (internal_url.EXAMPLE_COM, "Example Domain", does_not_raise()),
    (internal_url.EXAMPLE_COM, "no_match", pytest.raises(WaitForPageTitleToChangeTimeoutException)),
])
def test_wait_until_page_title_is(url: str, page_title: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url)
        browser.wait.until_page_title_is(page_title, timeout.VERY_SHORT) is not None
