import pytest
from _helper.xpath.method import (exception_handling_for_methods_with_2_arguments,
                                  exception_handling_for_methods_with_3_arguments_or_more)

from browserist import Browser
from browserist.browser.check_if.does_element_exist import check_if_does_element_exist
from browserist.browser.check_if.element_contains_text import check_if_element_contains_text
from browserist.browser.check_if.is_element_clickable import check_if_is_element_clickable
from browserist.browser.check_if.is_element_disabled import check_if_is_element_disabled
from browserist.browser.check_if.is_element_displayed import check_if_is_element_displayed
from browserist.browser.check_if.is_element_enabled import check_if_is_element_enabled
from browserist.browser.check_if.is_image_loaded import check_if_is_image_loaded
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    check_if_does_element_exist,
    check_if_is_element_clickable,
    check_if_is_element_disabled,
    check_if_is_element_displayed,
    check_if_is_element_enabled,
    check_if_is_image_loaded,
])
def test_xpath_exception_handling_for_check_if_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith2ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_2_arguments(browser_default_headless, method)


@pytest.mark.parametrize("method, text", [
    (check_if_element_contains_text, "More information..."),
])
def test_xpath_exception_handling_for_check_if_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    text: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, text)
