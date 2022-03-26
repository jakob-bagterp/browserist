import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS_W3SCHOOLS_COM_INPUT, exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.input.clear import input_clear
from browserist.browser.input.value import input_value
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable, BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [
    (input_clear, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_input_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout, url=internal_url.W3SCHOOLS_COM, tests=XPATH_TESTS_W3SCHOOLS_COM_INPUT)


@pytest.mark.parametrize("method, value, timeout", [
    (input_value, "search something", timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_input_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith4ArgumentsCallable,
    value: str,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, value, timeout, url=internal_url.W3SCHOOLS_COM, tests=XPATH_TESTS_W3SCHOOLS_COM_INPUT)
