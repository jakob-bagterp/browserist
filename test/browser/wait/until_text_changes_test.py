from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath, baseline_text, expectation", [
    ("/html/body/div/p[2]/a", "changed text", does_not_raise()),
    ("/html/body/div/p[2]/a", "More information...", pytest.raises(RetryTimeoutException)),
    ("/html/body/div/p[2]/a/div", "element doesn't exist", pytest.raises(WaitForElementTimeoutException)),
])
def test_wait_until_text_changes(xpath: str, baseline_text: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(internal_url.EXAMPLE_COM)
        browser.wait.until_text_changes(xpath, baseline_text, timeout.VERY_SHORT) is not None
