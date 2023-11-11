from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, CookieBannerSettings

from _config.combo.cookie_banner import COOKIE_BANNER_SETTINGS_WITH_IFRAME, COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME

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
