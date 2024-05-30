from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("xpath, expectation", [
    ("/html/body/section[2]/div[1]/a", does_not_raise()),
    ("/html/body/section[1]/div/h1", does_not_raise()),
    (does_not_exist.XPATH, pytest.raises(RetryTimeoutException)),
])
def test_wait_until_element_is_clickable(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        _ = browser.wait.until.is_clickable(xpath, timeout.VERY_SHORT) is not None
