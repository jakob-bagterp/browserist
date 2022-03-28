import pytest
from _helper.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.scroll.into_view import scroll_into_view
from browserist.browser.scroll.into_view_if_not_visible import scroll_into_view_if_not_visible
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    scroll_into_view,
    scroll_into_view_if_not_visible,
])
def test_xpath_exception_handling_for_scroll_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout.VERY_SHORT)
