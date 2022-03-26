import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS_W3SCHOOLS_COM_IMAGE, exception_handling_for_methods_with_3_arguments_or_more

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
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, timeout)


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
        browser_default_headless, method, timeout, url=internal_url.W3SCHOOLS_COM, tests=XPATH_TESTS_W3SCHOOLS_COM_IMAGE)
