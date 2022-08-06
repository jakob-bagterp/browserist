from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("xpath, expectation", [
    ("/html/body/div/p[2]/a", pytest.raises(RetryTimeoutException)),
    ("/html/body/div/p[2]/a/div", does_not_raise()),
])
def test_wait_until_element_disappears(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(internal_url.EXAMPLE_COM)
        _ = browser.wait.until.element_disappears(xpath, timeout.VERY_SHORT) is not None
