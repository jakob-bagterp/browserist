from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _constant.string import EMPTY_STRING
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.contact import MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize(
    "url, xpath, expectation",
    [
        (internal_url.MINI_SITE_CONTACT, MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, does_not_raise()),
        (internal_url.MINI_SITE_CONTACT, does_not_exist.XPATH, pytest.raises(WaitForElementTimeoutException)),
    ],
)
def test_clear_input_field_exceptions(
    url: str, xpath: str, expectation: Any, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(url)
        browser.input.clear(xpath, timeout.VERY_SHORT)


def test_clear_input_field(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_CONTACT)
    assert browser.get.attribute.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "value") == EMPTY_STRING
    search_input = "search input"
    browser.input.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, search_input, timeout.VERY_SHORT)
    assert browser.get.attribute.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "value") == search_input
    browser.input.clear(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, timeout.VERY_SHORT)
    assert browser.get.attribute.value(MINI_SITE_CONTACT_INPUT_SUBJECT_XPATH, "value") == EMPTY_STRING
