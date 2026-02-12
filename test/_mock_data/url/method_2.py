from typing import Any

from _helper.timeout import reset_to_not_timed_out
from _mock_data.url.model_2 import URLTestSet
from _mock_data.url.test_set_2 import URL_TEST_SET_DEFAULT

from browserist import Browser
from browserist.model.type.callable import (
    BrowserMethodWith2ArgumentsCallable,
    BrowserMethodWith3ArgumentsCallable,
    BrowserMethodWith4ArgumentsCallable,
)


def exception_handling_for_methods_with_2_arguments(
    browser: Browser, method: BrowserMethodWith2ArgumentsCallable, test_set: URLTestSet = URL_TEST_SET_DEFAULT
) -> None:
    browser = reset_to_not_timed_out(browser)
    for test in test_set.tests:
        with test.expectation:
            _ = method(browser._browser_driver, test.url) is not None


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable,
    *args: Any,
    test_set: URLTestSet = URL_TEST_SET_DEFAULT,
) -> None:
    browser = reset_to_not_timed_out(browser)
    for test in test_set.tests:
        with test.expectation:
            _ = method(browser._browser_driver, test.url, *args) is not None
