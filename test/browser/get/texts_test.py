import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_texts",
    [
        (internal_url.MINI_SITE_HOMEPAGE, MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, ["Learn more"]),
        (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[2]/div/h3", ["Feature 1", "Feature 2", "Feature 3"]),
        (internal_url.MINI_SITE_FEATURE_1, "/html/body/section[1]/div/p", ["Discover the features of our products."]),
        (
            internal_url.MINI_SITE_FEATURE_1,
            "//*[@id='main']/h2",
            ["Suspendisse vitae nibh ipsum", "Morbi sodales malesuada congue"],
        ),
    ],
)
def test_get_texts(url: str, xpath: str, expected_texts: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.texts(xpath) == expected_texts
