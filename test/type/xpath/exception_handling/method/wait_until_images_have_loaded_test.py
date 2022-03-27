import pytest
from _helper.xpath.method import exception_handling_for_methods_with_3_arguments_or_more
from _helper.xpath.test_set import XPATH_TEST_SET_W3SCHOOLS_COM_IMAGE

from browserist import Browser
from browserist.browser.wait.until_images_have_loaded import wait_until_images_have_loaded
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    wait_until_images_have_loaded,
])
def test_xpath_exception_handling_for_wait_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout.VERY_SHORT, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_IMAGE)
