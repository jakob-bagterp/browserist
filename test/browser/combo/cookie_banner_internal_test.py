from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.cookie_banner import DBA_ACCEPT_COOKIES, GOOGLE_ACCEPT_COOKIES
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url

from browserist import Browser, CookieBannerSettings


@pytest.mark.parametrize("url, cookie_banner_settings", [
    (external_url.DBA_DK, DBA_ACCEPT_COOKIES),
    (external_url.GOOGLE_COM, GOOGLE_ACCEPT_COOKIES),
])
def test_combo_cookie_banner_internal(
    url: str,
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(url)
        browser.combo.cookie_banner(cookie_banner_settings)
