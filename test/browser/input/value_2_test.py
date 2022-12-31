from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException

SEARCH_INPUT_XPATH = "//input[@id='search2']"


@pytest.mark.parametrize("url, xpath, expectation", [
    (internal_url.W3SCHOOLS_COM, SEARCH_INPUT_XPATH, does_not_raise()),
    (internal_url.W3SCHOOLS_COM, f"{SEARCH_INPUT_XPATH}/div", pytest.raises(WaitForElementTimeoutException)),
])
def test_input_value_exceptions(url: str, xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url)
        browser.input.value(xpath, "some text", timeout.VERY_SHORT)
