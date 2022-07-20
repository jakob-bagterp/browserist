import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_2_arguments
from _mock_data.xpath.test_set_3 import XPATH_TEST_SET_W3SCHOOLS_COM_IFRAME

from browserist import Browser
from browserist.browser.iframe.switch_to import switch_to_iframe
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable


@pytest.mark.parametrize("method", [
    switch_to_iframe,
])
def test_xpath_exception_handling_for_iframe_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
) -> None:
    exception_handling_for_methods_with_2_arguments(
        browser_default_headless, method, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_IFRAME)
