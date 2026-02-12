import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.dimensions import get_dimensions
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [(get_dimensions, timeout.VERY_SHORT)])
def test_xpath_exception_handling_for_get_dimensions_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable, timeout: float
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout)
