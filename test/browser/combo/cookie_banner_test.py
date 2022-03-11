from contextlib import nullcontext as does_not_raise

import pytest
from _config.combo.cookie_banner import DBA_ACCEPT_COOKIES, GOOGLE_ACCEPT_COOKIES
from _helper import external_url

from browserist import Browser, CookieBannerSettings


@pytest.mark.parametrize("url, cookie_banner_settings", [
    (external_url.DBA_DK, DBA_ACCEPT_COOKIES),
    (external_url.GOOGLE_COM, GOOGLE_ACCEPT_COOKIES),
])
def test_combo_cookie_banner(
    url: str,
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless: Browser
) -> None:

    with does_not_raise():
        browser = browser_default_headless
        browser.open.url(url)
        browser.combo.cookie_banner(cookie_banner_settings)
