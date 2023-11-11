from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.search import DBA_SEARCH, GOOGLE_SEARCH
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url

from browserist import Browser, SearchSettings


@pytest.mark.parametrize("url, term, search_settings", [
    (external_url.DBA_DK, "champagne", DBA_SEARCH),
    (external_url.GOOGLE_COM, "browserist github", GOOGLE_SEARCH),
])
def test_combo_search_external(
    url: str,
    term: str,
    search_settings: SearchSettings,
    browser_default_disable_images: Browser
) -> None:

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_disable_images)
        browser.open.url(url)
        browser.combo.search(term, search_settings)
