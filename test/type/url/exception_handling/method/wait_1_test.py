from _helper.external_url import GOOGLE_COM
from _helper.url.method_1 import exception_handling_for_methods_with_3_arguments_or_more
from _helper.url.test_set_1 import VALID_URL

from browserist import Browser
from browserist.browser.wait.until_url_changes import wait_until_url_changes
from browserist.browser.wait.until_url_is import wait_until_url_is
from browserist.constant import timeout


def test_url_exception_handling_for_wait_for_url_changes_methods(browser_default_headless: Browser) -> None:
    browser_default_headless.open.url(GOOGLE_COM)
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, wait_until_url_changes, timeout.VERY_SHORT)


def test_url_exception_handling_for_wait_for_url_is_method(browser_default_headless: Browser) -> None:
    browser_default_headless.open.url(VALID_URL)
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, wait_until_url_is, timeout.VERY_SHORT)
