import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_urls",
    [
        (
            internal_url.MINI_SITE_HOMEPAGE,
            MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH,
            [internal_url.MINI_SITE_FEATURE_1],
        ),
        (
            internal_url.MINI_SITE_HOMEPAGE,
            "/html/body/section[2]/div/a",
            [internal_url.MINI_SITE_FEATURE_1, internal_url.MINI_SITE_FEATURE_2, internal_url.MINI_SITE_FEATURE_3],
        ),
        (
            internal_url.MINI_SITE_HOMEPAGE,
            "/html/body/header/nav/ul/li/a",
            [internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_ABOUT, internal_url.MINI_SITE_CONTACT],
        ),
        (
            internal_url.MINI_SITE_FEATURE_1,
            "/html/body/footer/nav/ul/li/a",
            [internal_url.MINI_SITE_ABOUT, internal_url.MINI_SITE_CONTACT],
        ),
    ],
)
def test_get_url_from_links(url: str, xpath: str, expected_urls: list[str], browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.from_links(xpath) == expected_urls
