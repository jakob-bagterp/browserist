from typing import Any

from _helper.url.model_1 import URLTestSet
from _helper.url.test_set_1 import URL_TEST_SET_DEFAULT

from browserist import Browser
from browserist.model.type.callable import (BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable,
                                            BrowserMethodWith4ArgumentsCallable)


def exception_handling_for_methods_with_2_arguments(
    browser: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
    test_set: URLTestSet = URL_TEST_SET_DEFAULT
) -> None:
    for test in test_set.tests:
        with test.expactation:
            _ = method(browser.driver, test.url) is not None


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable,
    *args: Any,
    test_set: URLTestSet = URL_TEST_SET_DEFAULT
) -> None:
    for test in test_set.tests:
        with test.expactation:
            _ = method(browser.driver, test.url, *args) is not None
