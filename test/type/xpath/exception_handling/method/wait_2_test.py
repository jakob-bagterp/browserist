import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.xpath.test_set_3 import (XPATH_TEST_SET_MINI_SITE_FEATURE_1_IMAGE,
                                         XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK, XPATH_TEST_SET_W3SCHOOLS_COM_HEADLINE)

from browserist import Browser
from browserist.browser.wait.for_element import wait_for_element
from browserist.browser.wait.until.contains_any_text import wait_until_element_contains_any_text
from browserist.browser.wait.until.element_disappears import wait_until_element_disappears
from browserist.browser.wait.until.is_clickable import wait_until_element_is_clickable
from browserist.browser.wait.until.text.changes import wait_until_text_changes
from browserist.browser.wait.until.text.contains import wait_until_text_contains
from browserist.browser.wait.until.text.equals import wait_until_text_equals
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable, BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize("method", [
    wait_for_element,
    wait_until_element_disappears,
])
def test_xpath_exception_handling_for_wait_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_MINI_SITE_FEATURE_1_IMAGE)


@pytest.mark.parametrize("method, text", [
    (wait_until_text_changes, "not same text as button"),
    (wait_until_text_contains, "information"),
    (wait_until_text_equals, "More information..."),
])
def test_xpath_exception_handling_for_wait_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith4ArgumentsCallable,
    text: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, text, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK)


@pytest.mark.parametrize("method", [
    wait_until_element_contains_any_text,
])
def test_xpath_exception_handling_for_wait_methods_3(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_HEADLINE)


@pytest.mark.parametrize("method", [
    wait_until_element_is_clickable,
])
def test_xpath_exception_handling_for_wait_methods_4(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK)
