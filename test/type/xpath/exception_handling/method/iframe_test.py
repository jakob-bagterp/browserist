import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.xpath.test_set_3 import XPATH_TEST_SET_COOKIE_BANNER_IFRAME

from browserist import Browser
from browserist.browser.iframe.switch_to import switch_to_iframe
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [(switch_to_iframe, timeout.VERY_SHORT)])
def test_xpath_exception_handling_for_iframe_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable, timeout: float
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout, test_set=XPATH_TEST_SET_COOKIE_BANNER_IFRAME
    )
