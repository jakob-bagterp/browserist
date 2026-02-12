import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

MINI_SITE_HOMEPAGE_WITH_PARAMETERS = f"{internal_url.MINI_SITE_HOMEPAGE}?foo=bar"


@pytest.mark.parametrize(
    "url1, url2, ignore_parameters, expected_url",
    [
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, True, internal_url.MINI_SITE_HOMEPAGE),
        (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, False, internal_url.MINI_SITE_HOMEPAGE),
        (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_WITH_PARAMETERS, True, internal_url.MINI_SITE_HOMEPAGE),
        (
            internal_url.MINI_SITE_HOMEPAGE,
            MINI_SITE_HOMEPAGE_WITH_PARAMETERS,
            False,
            MINI_SITE_HOMEPAGE_WITH_PARAMETERS,
        ),
    ],
)
def test_open_url_if_not_current_ignore_parameters(
    url1: str, url2: str, ignore_parameters: bool, expected_url: str, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url1)
    get_url1 = browser.get.url.current()
    assert get_url1 == url1
    browser.open.url_if_not_current(url2, ignore_parameters=ignore_parameters)
    get_url2 = browser.get.url.current()
    assert get_url2 == expected_url
