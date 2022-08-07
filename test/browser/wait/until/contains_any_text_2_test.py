from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("xpath, expectation", [
    ("/html/body/div[5]/div[9]/div/div/div[3]/img", pytest.raises(RetryTimeoutException)),
    ("/html/body/div[5]/div[1]/div/h1", does_not_raise()),
])
def test_wait_until_element_contains_any_text(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(internal_url.W3SCHOOLS_COM)
        _ = browser.wait.until.contains_any_text(xpath, timeout.VERY_SHORT) is not None
