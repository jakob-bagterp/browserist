from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _constant.string import EMPTY_STRING
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("url, xpath, expectation", [
    (internal_url.MINI_SITE_CONTACT, "//input[@id='subject']", does_not_raise()),
    (internal_url.MINI_SITE_CONTACT, does_not_exist.XPATH, pytest.raises(WaitForElementTimeoutException)),
])
def test_clear_input_field_exceptions(url: str, xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url)
        browser.input.clear(xpath, timeout.VERY_SHORT)


def test_clear_input_field(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_CONTACT)
    assert browser.get.attribute.value("//input[@id='subject']", "value") == EMPTY_STRING
    search_input = "search input"
    browser.input.value("//input[@id='subject']", search_input, timeout.VERY_SHORT)
    assert browser.get.attribute.value("//input[@id='subject']", "value") == search_input
    browser.input.clear("//input[@id='subject']", timeout.VERY_SHORT)
    assert browser.get.attribute.value("//input[@id='subject']", "value") == EMPTY_STRING
