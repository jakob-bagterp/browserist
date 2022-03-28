import pytest
from _helper.xpath.method import exception_handling_for_methods_with_3_arguments_or_more
from _helper.xpath.test_set_2 import XPATH_TEST_SET_W3SCHOOLS_COM_INPUT

from browserist import Browser
from browserist.browser.input.clear import input_clear
from browserist.browser.input.value import input_value
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable, BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize("method", [
    input_clear,
])
def test_xpath_exception_handling_for_input_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_INPUT)


@pytest.mark.parametrize("method, value", [
    (input_value, "search something"),
])
def test_xpath_exception_handling_for_input_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith4ArgumentsCallable,
    value: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, value, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_INPUT)
