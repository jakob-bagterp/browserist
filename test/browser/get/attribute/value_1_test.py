import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.feature_1 import MINI_SITE_FEATURE_1_IMAGE_1_XPATH
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, attribute, expected_attribute",
    [
        (
            internal_url.MINI_SITE_HOMEPAGE,
            MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH,
            "href",
            internal_url.MINI_SITE_FEATURE_1,
        ),
        (internal_url.MINI_SITE_HOMEPAGE, "/html/head/meta[3]", "name", "viewport"),
        (
            internal_url.MINI_SITE_FEATURE_1,
            MINI_SITE_FEATURE_1_IMAGE_1_XPATH,
            "src",
            internal_url.MINI_SITE_IMAGE_LAB_SAMPLES,
        ),
        (internal_url.MINI_SITE_FEATURE_1, "/html/head/link[1]", "rel", "stylesheet"),
        (internal_url.MINI_SITE_FEATURE_1, "/html/body/section[1]/div", "class", "hero__text-box"),
    ],
)
def test_get_attribute_value(
    url: str, xpath: str, attribute: str, expected_attribute: str, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.attribute.value(xpath, attribute) == expected_attribute
