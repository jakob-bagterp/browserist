import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS_W3SCHOOLS_COM_IMAGE, exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.wait.for_element import wait_for_element
from browserist.browser.wait.until_element_disappears import wait_until_element_disappears
from browserist.browser.wait.until_images_have_loaded import wait_until_images_have_loaded
from browserist.browser.wait.until_text_changes import wait_until_text_changes
from browserist.browser.wait.until_text_contains import wait_until_text_contains
from browserist.browser.wait.until_text_is import wait_until_text_is
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable, BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize("method", [
    wait_for_element,
    wait_until_element_disappears,
    wait_until_images_have_loaded,
])
def test_xpath_exception_handling_for_wait_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, url=internal_url.W3SCHOOLS_COM, tests=XPATH_TESTS_W3SCHOOLS_COM_IMAGE)


@pytest.mark.parametrize("method, text", [
    (wait_until_text_changes, "not same text as button"),
    (wait_until_text_contains, "information"),
    (wait_until_text_is, "More information..."),
])
def test_xpath_exception_handling_for_wait_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith4ArgumentsCallable,
    text: str
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, text, timeout.VERY_SHORT)
