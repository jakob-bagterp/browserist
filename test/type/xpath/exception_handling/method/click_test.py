import pytest
from _helper.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.click.button import click_button
from browserist.browser.click.button_if_contains_text import click_button_if_contains_text
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    click_button,
])
def test_xpath_exception_handling_for_click_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout.VERY_SHORT)


@pytest.mark.parametrize("method, text", [
    (click_button_if_contains_text, "More information..."),
])
def test_xpath_exception_handling_for_click_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    text: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, text, timeout.VERY_SHORT)
