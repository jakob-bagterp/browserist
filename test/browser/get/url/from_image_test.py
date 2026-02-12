import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.feature_1 import MINI_SITE_FEATURE_1_IMAGE_1_XPATH

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_url",
    [(internal_url.MINI_SITE_FEATURE_1, MINI_SITE_FEATURE_1_IMAGE_1_XPATH, internal_url.MINI_SITE_IMAGE_LAB_SAMPLES)],
)
def test_get_url_from_image(url: str, xpath: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.from_image(xpath) == expected_url
