import pytest
from _mock_data.xpath.method_3 import (
    exception_handling_for_methods_with_2_arguments,
    exception_handling_for_methods_with_3_arguments_or_more,
)

from browserist import Browser
from browserist.browser.check_if.contains_any_text import check_if_contains_any_text
from browserist.browser.check_if.contains_text import check_if_contains_text
from browserist.browser.check_if.does_exist import check_if_does_exist
from browserist.browser.check_if.is_clickable import check_if_is_clickable
from browserist.browser.check_if.is_disabled import check_if_is_disabled
from browserist.browser.check_if.is_displayed import check_if_is_displayed
from browserist.browser.check_if.is_enabled import check_if_is_enabled
from browserist.browser.check_if.is_image_loaded import check_if_is_image_loaded
from browserist.browser.check_if.is_selected import check_if_is_selected
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable, BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize(
    "method",
    [
        check_if_is_image_loaded,
        check_if_contains_any_text,
        check_if_does_exist,
        check_if_is_clickable,
        check_if_is_disabled,
        check_if_is_displayed,
        check_if_is_enabled,
        check_if_is_selected,
    ],
)
def test_xpath_exception_handling_for_check_if_methods_1(
    browser_default_headless: Browser, method: BrowserMethodWith2ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_2_arguments(browser_default_headless, method)


@pytest.mark.parametrize("method, text, ignore_case", [(check_if_contains_text, "More information...", True)])
def test_xpath_exception_handling_for_check_if_methods_2(
    browser_default_headless: Browser, method: BrowserMethodWith4ArgumentsCallable, text: str, ignore_case: bool
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, text, ignore_case)
