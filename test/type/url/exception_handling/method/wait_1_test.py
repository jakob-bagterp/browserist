import pytest
from _helper.url.method_1 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.wait.until_url_changes import wait_until_url_changes
from browserist.browser.wait.until_url_is import wait_until_url_is
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    wait_until_url_changes,
    wait_until_url_is,
])
def test_xpath_exception_handling_for_wait_for_url_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout.VERY_SHORT)
