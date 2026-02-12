import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url, internal_url

from browserist import Browser, helper


@pytest.mark.parametrize(
    "url1, url2",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_FEATURE_1),
        (internal_url.MINI_SITE_FEATURE_1, external_url.EXAMPLE_COM),
        (external_url.EXAMPLE_COM, external_url.IANA_ORG_RESERVED_DOMAINS),
    ],
)
def test_open_url(url1: str, url2: str, browser_default_headless: Browser) -> None:
    url1 = helper.url.ensure_trailing_slash(url1)
    url2 = helper.url.ensure_trailing_slash(url2)
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url1)
    get_url1 = helper.url.ensure_trailing_slash(browser.get.url.current())
    browser.open.url(url2)
    get_url2 = helper.url.ensure_trailing_slash(browser.get.url.current())
    assert get_url1 == url1
    assert get_url2 == url2
    assert get_url1 != get_url2
