import pytest
from _helper.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.text.from_element import get_text_from_element
from browserist.browser.get.text.from_multiple_elements import get_text_from_multiple_elements
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [
    (get_text_from_element, timeout.VERY_SHORT),
    (get_text_from_multiple_elements, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_get_text_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout)
