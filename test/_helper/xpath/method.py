from typing import Any

from _helper.xpath.model import XPathTestSet
from _helper.xpath.test_set import XPATH_TEST_SET_EXAMPLE_COM_DEFAULT

from browserist import Browser
from browserist.model.type.callable import (BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable,
                                            BrowserMethodWith4ArgumentsCallable)


def exception_handling_for_methods_with_2_arguments(
    browser: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
    test_set: XPathTestSet = XPATH_TEST_SET_EXAMPLE_COM_DEFAULT
) -> None:
    browser.open.url(test_set.url)
    for test in test_set.tests:
        with test.expactation:
            _ = method(browser.driver, test.xpath) is not None


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable,
    *args: Any,
    test_set: XPathTestSet = XPATH_TEST_SET_EXAMPLE_COM_DEFAULT
) -> None:
    browser.open.url(test_set.url)
    for test in test_set.tests:
        with test.expactation:
            _ = method(browser.driver, test.xpath, *args) is not None
