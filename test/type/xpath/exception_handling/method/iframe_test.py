import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS_W3SCHOOLS_COM_IFRAME, exception_handling_for_methods_with_2_arguments

from browserist import Browser
from browserist.browser.iframe.iframe import switch_to_iframe
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable


@pytest.mark.parametrize("method", [
    switch_to_iframe,
])
def test_xpath_exception_handling_for_iframe_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
) -> None:
    exception_handling_for_methods_with_2_arguments(
        browser_default_headless, method, url=internal_url.W3SCHOOLS_COM, tests=XPATH_TESTS_W3SCHOOLS_COM_IFRAME)
