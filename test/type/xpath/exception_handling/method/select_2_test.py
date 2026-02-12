import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.xpath.test_set_3 import XPATH_TEST_SET_MINI_SITE_CONTACT_INPUT

from browserist import Browser
from browserist.browser.input.select import select_input_field
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [select_input_field])
def test_xpath_exception_handling_for_select_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_MINI_SITE_CONTACT_INPUT
    )
