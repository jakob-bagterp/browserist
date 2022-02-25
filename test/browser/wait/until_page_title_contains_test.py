from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForPageTitleToChangeTimeoutException


@pytest.mark.parametrize("url, page_title_fragment, expectation", [
    (internal_url.EXAMPLE_COM, "Example", does_not_raise()),
    (internal_url.EXAMPLE_COM, "no_match", pytest.raises(WaitForPageTitleToChangeTimeoutException)),
])
def test_wait_until_page_title_contains(url: str, page_title_fragment: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url)
        browser.wait.until_page_title_contains(page_title_fragment, timeout.VERY_SHORT) is not None
