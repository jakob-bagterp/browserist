from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS, XPATH_TESTS_EXAMPLE_COM

from browserist import Browser
from browserist.browser.check_if.does_element_exist import check_if_does_element_exist
from browserist.browser.check_if.element_contains_text import check_if_element_contains_text
from browserist.browser.check_if.is_element_clickable import check_if_is_element_clickable
from browserist.browser.check_if.is_element_disabled import check_if_is_element_disabled
from browserist.browser.check_if.is_element_displayed import check_if_is_element_displayed
from browserist.browser.check_if.is_element_enabled import check_if_is_element_enabled
from browserist.browser.check_if.is_image_loaded import check_if_is_image_loaded
from browserist.browser.click.button import click_button
from browserist.browser.click.button_if_contains_text import click_button_if_contains_text
from browserist.browser.get.attribute.value import get_attribute_value
from browserist.browser.get.attribute.value_from_multiple_elements import get_attribute_value_from_multiple_elements
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    check_if_does_element_exist,
    check_if_is_element_clickable,
    check_if_is_element_disabled,
    check_if_is_element_displayed,
    check_if_is_element_enabled,
    check_if_is_image_loaded,
    click_button,
])
def test_xpath_exception_handling_for_methods_with_2_arguments(
    method: BrowserMethodWith2ArgumentsCallable,
    browser_default_headless: Browser
) -> None:

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    for test in XPATH_TESTS:
        with test.expactation:
            _ = method(browser.driver, test.xpath) is not None


@pytest.mark.parametrize("method, arg3", [
    (check_if_element_contains_text, "More information..."),
    (click_button_if_contains_text, "More information..."),
    (get_attribute_value, "href"),
    (get_attribute_value_from_multiple_elements, "href"),
])
def test_xpath_exception_handling_for_methods_with_3_arguments(
    method: BrowserMethodWith3ArgumentsCallable,
    arg3: Any,
    browser_default_headless: Browser
) -> None:

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    for test in XPATH_TESTS_EXAMPLE_COM:
        with test.expactation:
            _ = method(browser.driver, test.xpath, arg3) is not None
