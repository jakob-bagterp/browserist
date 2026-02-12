import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.attribute.value import get_attribute_value
from browserist.browser.get.attribute.values import get_attribute_values
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize(
    "method, attribute, timeout",
    [(get_attribute_value, "href", timeout.VERY_SHORT), (get_attribute_values, "href", timeout.VERY_SHORT)],
)
def test_xpath_exception_handling_for_get_attribute_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable, attribute: str, timeout: float
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, attribute, timeout)
