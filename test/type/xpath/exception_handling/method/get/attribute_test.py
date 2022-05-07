import pytest
from _mock_data.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.attribute.value import get_attribute_value
from browserist.browser.get.attribute.values import get_attribute_values
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, attribute", [
    (get_attribute_value, "href"),
    (get_attribute_values, "href"),
])
def test_xpath_exception_handling_for_get_attribute_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    attribute: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, attribute)
