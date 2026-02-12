from _mock_data.url.external_url import GOOGLE_COM
from _mock_data.url.method_2 import exception_handling_for_methods_with_3_arguments_or_more
from _mock_data.url.test_set_2 import VALID_URL

from browserist import Browser
from browserist.browser.wait.until.url.changes import wait_until_url_changes
from browserist.browser.wait.until.url.equals import wait_until_url_equals
from browserist.constant import timeout


def test_url_exception_handling_for_wait_for_url_changes_methods(browser_default_headless: Browser) -> None:
    browser_default_headless.open.url(GOOGLE_COM)
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, wait_until_url_changes, timeout.VERY_SHORT
    )


def test_url_exception_handling_for_wait_for_url_is_method(browser_default_headless: Browser) -> None:
    browser_default_headless.open.url(VALID_URL)
    exception_handling_for_methods_with_3_arguments_or_more(
        browser_default_headless, wait_until_url_equals, timeout.VERY_SHORT
    )
