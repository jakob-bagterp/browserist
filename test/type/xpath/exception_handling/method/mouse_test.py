import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.mouse.hover import mouse_hover
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [mouse_hover])
def test_xpath_exception_handling_for_mouse_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout.VERY_SHORT)
