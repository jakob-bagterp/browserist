import pytest
from _helper.xpath.method import exception_handling_for_methods_with_2_arguments

from browserist import Browser
from browserist.browser.mouse.hover import mouse_hover
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable


@pytest.mark.parametrize("method", [
    mouse_hover,
])
def test_xpath_exception_handling_for_mouse_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
) -> None:
    exception_handling_for_methods_with_2_arguments(browser_default_headless, method)
