from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.cookie_banner import DBA_ACCEPT_COOKIES, GOOGLE_ACCEPT_COOKIES
from _config.combo.search import DBA_SEARCH, GOOGLE_SEARCH
from _helper import external_url

from browserist import Browser, CookieBannerSettings, SearchSettings


@pytest.mark.parametrize("url, term, search_settings, cookie_banner_settings", [
    (external_url.DBA_DK, "champagne", DBA_SEARCH, DBA_ACCEPT_COOKIES),
    (external_url.GOOGLE_COM, "browserist github", GOOGLE_SEARCH, GOOGLE_ACCEPT_COOKIES),
])
def test_combo_search(
    url: str,
    term: str,
    search_settings: SearchSettings,
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_images_disabled: Browser
) -> None:

    with expectation_of_no_exceptions_raised():
        browser = browser_default_headless_images_disabled
        browser.open.url(url)
        browser.combo.cookie_banner(cookie_banner_settings)
        browser.combo.search(term, search_settings)
