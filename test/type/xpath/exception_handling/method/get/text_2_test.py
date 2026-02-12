import pytest
from _mock_data.xpath.method_3 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.get.text import get_text
from browserist.browser.get.texts import get_texts
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [(get_text, timeout.VERY_SHORT), (get_texts, timeout.VERY_SHORT)])
def test_xpath_exception_handling_for_get_text_methods(
    browser_default_headless: Browser, method: BrowserMethodWith3ArgumentsCallable, timeout: float
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout)
