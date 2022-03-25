import pytest
from _helper import internal_url
from _helper.xpath import XPATH_TESTS

from browserist import Browser
from browserist.browser.check_if.does_element_exist import check_if_does_element_exist
# from browserist.browser.check_if.element_contains_text import element_contains_text  # TODO: Add test of methods with 3 arguments.
from browserist.browser.check_if.is_element_clickable import check_if_is_element_clickable
from browserist.browser.check_if.is_element_disabled import check_if_is_element_disabled
from browserist.browser.check_if.is_element_displayed import check_if_is_element_displayed
from browserist.browser.check_if.is_element_enabled import check_if_is_element_enabled
from browserist.browser.check_if.is_image_loaded import check_if_is_image_loaded
from browserist.model.type.callable import BrowserMethodWith2ArgumentsCallable


@pytest.mark.parametrize("method", [
    check_if_does_element_exist,
    check_if_is_element_clickable,
    check_if_is_element_disabled,
    check_if_is_element_displayed,
    check_if_is_element_enabled,
    check_if_is_image_loaded,
])
def test_xpath_exception_handling_for_methods_with_2_arguments(
    method: BrowserMethodWith2ArgumentsCallable,
    browser_default_headless: Browser
) -> None:

    browser = browser_default_headless
    browser.open.url_if_not_current(internal_url.EXAMPLE_COM)
    for test in XPATH_TESTS:
        with test.expactation:
            _ = method(browser.driver, test.xpath) is not None
