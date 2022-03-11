from contextlib import nullcontext as does_not_raise

from _config.combo.cookie_banner import DBA_ACCEPT_COOKIES
from _helper import external_url

from browserist import Browser


def test_wait_for_element(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with does_not_raise():
        browser.open.url(external_url.DBA_DK)
        browser.combo.cookie_banner(DBA_ACCEPT_COOKIES)
