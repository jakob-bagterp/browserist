from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, CookieBannerSettings

HAS_LOADED_XPATH = "//*[@id='cookie-banner']"

ACCEPT_BUTTON_XPATH = "//button[@id='accept-cookies']"

COOKIE_BANNER_SETTINGS_WITH_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath="//iframe[@id='cookie-banner-iframe']",
    has_loaded_xpath=HAS_LOADED_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=HAS_LOADED_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)


@pytest.mark.parametrize("cookie_banner_settings", [
    COOKIE_BANNER_SETTINGS_WITH_IFRAME,
    COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME,
])
def test_combo_cookie_banner_internal(
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.combo.cookie_banner(cookie_banner_settings)


PAGE_HEADER_TEXT = "Welcome to the Cookie Banner Test Website"

PAGE_HEADER_XPATH = "/html/body/main/h1"


def test_combo_cookie_banner_internal_return_iframe_to_origin(
    browser_default_headless_disable_images: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_disable_images)
    browser.open.url(internal_url.COOKIE_BANNER_WITH_IFRAME)
    assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)
    browser.combo.cookie_banner(COOKIE_BANNER_SETTINGS_WITH_IFRAME)
    assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)
