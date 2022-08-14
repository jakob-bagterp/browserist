from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath, regex, expectation", [
    ("/html/body/div/p[2]/a", "More information...", does_not_raise()),
    ("/html/body/div/p[2]/a", "mOrE iNfoRmaTion...", does_not_raise()),
    ("/html/body/div/p[2]/a", "information", does_not_raise()),
    ("/html/body/div/p[2]/a", r"^information", pytest.raises(RetryTimeoutException)),
    ("/html/body/div/p[2]/a", "no valid text", pytest.raises(RetryTimeoutException)),
    ("/html/body/div/p[2]/a/div", "element doesn't exist", pytest.raises(WaitForElementTimeoutException)),
])
def test_wait_until_text_contains(xpath: str, regex: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.EXAMPLE_COM)
        _ = browser.wait.until.text.contains(xpath, regex, timeout.VERY_SHORT) is not None
