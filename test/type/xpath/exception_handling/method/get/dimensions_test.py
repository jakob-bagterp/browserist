import pytest
from _helper.xpath.method import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.dimensions_of_element import get_dimensions_of_element
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [
    (get_dimensions_of_element, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_get_dimensions_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout)
