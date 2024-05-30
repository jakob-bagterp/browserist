from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath, expectation", [
    ("/html/body/section[2]/div[1]/a", does_not_raise()),
    (does_not_exist.XPATH, pytest.raises(WaitForElementTimeoutException)),
])
def test_wait_for_element(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    with expectation:
        _ = browser.wait.for_element(xpath, timeout.VERY_SHORT) is not None
