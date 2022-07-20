from typing import Any

from _mock_data.file_png.model_1 import FilePNGTestSet
from _mock_data.file_png.test_set_1 import FILE_PNG_TEST_SET_DEFAULT

from browserist import Browser
from browserist.model.type.callable import (BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable,
                                            BrowserMethodWith4ArgumentsCallable)


def exception_handling_for_methods_with_2_arguments(
    browser: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
    test_set: FilePNGTestSet = FILE_PNG_TEST_SET_DEFAULT
) -> None:
    for test in test_set.tests:
        with test.expactation:
            _ = method(browser.driver, "") is not None  # TODO: Update this snippet to use the new exception handling.


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable,
    *args: Any,
    test_set: FilePNGTestSet = FILE_PNG_TEST_SET_DEFAULT
) -> None:
    for test in test_set.tests:
        with test.expactation:
            # TODO: Update this snippet to use the new exception handling.
            _ = method(browser.driver, "", *args) is not None
