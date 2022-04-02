import pytest
from _mock_data.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.xpath.test_set_2 import XPATH_TEST_SET_EXAMPLE_COM_LINK, XPATH_TEST_SET_W3SCHOOLS_COM_IMAGE

from browserist import Browser
from browserist.browser.get.url.from_image import get_url_from_image
from browserist.browser.get.url.from_link import get_url_from_link
from browserist.browser.get.url.from_multiple_images import get_url_from_multiple_images
from browserist.browser.get.url.from_multiple_links import get_url_from_multiple_links
from browserist.constant import timeout
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method, timeout", [
    (get_url_from_link, timeout.VERY_SHORT),
    (get_url_from_multiple_links, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_get_url_methods_1(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout, test_set=XPATH_TEST_SET_EXAMPLE_COM_LINK)


@pytest.mark.parametrize("method, timeout", [
    (get_url_from_image, timeout.VERY_SHORT),
    (get_url_from_multiple_images, timeout.VERY_SHORT),
])
def test_xpath_exception_handling_for_get_url_methods_2(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    timeout: int
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, method, timeout, test_set=XPATH_TEST_SET_W3SCHOOLS_COM_IMAGE)
