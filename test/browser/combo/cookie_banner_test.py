from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.cookie_banner import COOKIE_BANNER_SETTINGS_WITH_IFRAME, COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, CookieBannerSettings


@pytest.mark.parametrize("cookie_banner_settings", [
    COOKIE_BANNER_SETTINGS_WITH_IFRAME,
    COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME,
])
def test_combo_cookie_banner(
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.combo.cookie_banner(cookie_banner_settings)


PAGE_HEADER_TEXT = "Welcome to the Cookie Banner Test Website"

PAGE_HEADER_XPATH = "/html/body/main/h1"


def test_combo_cookie_banner_return_iframe_to_origin(
    browser_default_headless_disable_images: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_disable_images)
    browser.open.url(internal_url.COOKIE_BANNER_WITH_IFRAME)
    assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)
    browser.combo.cookie_banner(COOKIE_BANNER_SETTINGS_WITH_IFRAME)
    assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)
