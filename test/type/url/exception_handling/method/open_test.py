import pytest
from _mock_data.url.method_2 import exception_handling_for_methods_with_2_arguments

from browserist import Browser
from browserist.browser.open.url import open_url
from browserist.browser.open.url_if_not_current import open_url_if_not_current
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable


@pytest.mark.parametrize("method", [open_url, open_url_if_not_current])
def test_url_exception_handling_for_open_url_methods(
    browser_default_headless: Browser, method: BrowserMethodWith2ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_2_arguments(browser_default_headless, method)
