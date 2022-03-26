from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS, XPATH_TESTS_EXAMPLE_COM

from browserist import Browser
from browserist.browser.click.button import click_button
from browserist.browser.click.button_if_contains_text import click_button_if_contains_text
from browserist.browser.get.attribute.value import get_attribute_value
from browserist.browser.get.attribute.value_from_multiple_elements import get_attribute_value_from_multiple_elements
from browserist.browser.get.text.from_element import get_text_from_element
from browserist.browser.get.text.from_multiple_elements import get_text_from_multiple_elements
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
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
    (click_button_if_contains_text, "More information..."),
    (get_attribute_value, "href"),
    (get_attribute_value_from_multiple_elements, "href"),
    (get_text_from_element, timeout.VERY_SHORT),
    (get_text_from_multiple_elements, timeout.VERY_SHORT),
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
