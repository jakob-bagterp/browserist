import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.xpath.test_set_3 import XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK

from browserist import Browser
from browserist.browser.click.button import click_button
from browserist.browser.click.button_if_contains_text import click_button_if_contains_text
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable, BrowserMethodWith5ArgumentsCallable


@pytest.mark.parametrize("method", [click_button])
def test_xpath_exception_handling_for_click_methods_1(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout.VERY_SHORT)


@pytest.mark.parametrize(
    "method, text, ignore_case, timeout", [(click_button_if_contains_text, "Learn more", True, timeout.VERY_SHORT)]
)
def test_xpath_exception_handling_for_click_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith5ArgumentsCallable,
    text: str,
    ignore_case: bool,
    timeout: float,
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, text, ignore_case, timeout, test_set=XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK
    )
