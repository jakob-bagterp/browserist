import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

MINI_SITE_HOMEPAGE_WITH_TRAILING_SLASH = f"{internal_url.MINI_SITE_HOMEPAGE}/"


@pytest.mark.parametrize(
    "url1, url2, ignore_trailing_slash, expected_url",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, True, internal_url.MINI_SITE_HOMEPAGE),
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, False, internal_url.MINI_SITE_HOMEPAGE),
        (
            internal_url.MINI_SITE_HOMEPAGE,
            MINI_SITE_HOMEPAGE_WITH_TRAILING_SLASH,
            True,
            internal_url.MINI_SITE_HOMEPAGE,
        ),
        (
            internal_url.MINI_SITE_HOMEPAGE,
            MINI_SITE_HOMEPAGE_WITH_TRAILING_SLASH,
            False,
            MINI_SITE_HOMEPAGE_WITH_TRAILING_SLASH,
        ),
    ],
)
def test_open_url_if_not_current_ignore_trailing_slash(
    url1: str, url2: str, ignore_trailing_slash: bool, expected_url: str, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url1)
    get_url1 = browser.get.url.current()
    assert get_url1 == url1
    browser.open.url_if_not_current(url2, ignore_trailing_slash=ignore_trailing_slash)
    get_url2 = browser.get.url.current()
    assert get_url2 == expected_url
