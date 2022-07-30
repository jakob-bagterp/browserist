from typing import Any

from _mock_data.xpath.model_3 import XPathTestSet
from _mock_data.xpath.test_set_3 import XPATH_TEST_SET_EXAMPLE_COM_DEFAULT

from browserist import Browser
from browserist.model.type.callable import (BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable,
                                            BrowserMethodWith4ArgumentsCallable, BrowserMethodWith5ArgumentsCallable)


def exception_handling_for_methods_with_2_arguments(
    browser: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
    test_set: XPathTestSet = XPATH_TEST_SET_EXAMPLE_COM_DEFAULT
) -> None:
    browser.open.url(test_set.url)
    for test in test_set.tests:
        with test.expectation:
            _ = method(browser.driver, test.xpath) is not None


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable | BrowserMethodWith5ArgumentsCallable,
    *args: Any,
    test_set: XPathTestSet = XPATH_TEST_SET_EXAMPLE_COM_DEFAULT
) -> None:
    browser.open.url(test_set.url)
    for test in test_set.tests:
        with test.expectation:
            _ = method(browser.driver, browser._browser_driver.settings, test.xpath, *args) is not None


def exception_handling_for_screenshot_methods(
    browser: Browser,
    method: BrowserMethodWith5ArgumentsCallable,
    file_name: str,
    temp_dir: str,
    test_set: XPathTestSet = XPATH_TEST_SET_EXAMPLE_COM_DEFAULT,
) -> None:
    browser.open.url(test_set.url)
    for test in test_set.tests:
        with test.expectation:
            _ = method(browser.driver, browser._browser_driver.settings, test.xpath, file_name, temp_dir) is not None
