from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _constant.string import EMPTY_STRING
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath import xpath

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("url, xpath, expectation", [
    (internal_url.W3SCHOOLS_COM, xpath.w3schools_com.SEARCH_INPUT, does_not_raise()),
    (internal_url.W3SCHOOLS_COM, f"{xpath.w3schools_com.SEARCH_INPUT}/div", pytest.raises(WaitForElementTimeoutException)),
])
def test_clear_input_field_exceptions(url: str, xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url)
        browser.input.clear(xpath, timeout.VERY_SHORT)


def test_clear_input_field(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.get.attribute.value(xpath.w3schools_com.SEARCH_INPUT, "value") == EMPTY_STRING
    search_input = "search input"
    browser.input.value(xpath.w3schools_com.SEARCH_INPUT, search_input, timeout.VERY_SHORT)
    assert browser.get.attribute.value(xpath.w3schools_com.SEARCH_INPUT, "value") == search_input
    browser.input.clear(xpath.w3schools_com.SEARCH_INPUT, timeout.VERY_SHORT)
    assert browser.get.attribute.value(xpath.w3schools_com.SEARCH_INPUT, "value") == EMPTY_STRING
