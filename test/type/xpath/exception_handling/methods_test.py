from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS_EXAMPLE_COM

from browserist import Browser
from browserist.browser.get.text.from_element import get_text_from_element
from browserist.browser.get.text.from_multiple_elements import get_text_from_multiple_elements
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, arg3", [
    (get_text_from_element, timeout.VERY_SHORT),
    (get_text_from_multiple_elements, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_methods_with_3_arguments(
    method: BrowserMethodWith3ArgumentsCallable,
    arg3: Any,
    browser_default_headless: Browser
) -> None:

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    for test in XPATH_TESTS_EXAMPLE_COM:
        with test.expactation:
            _ = method(browser.driver, test.xpath, arg3) is not None
