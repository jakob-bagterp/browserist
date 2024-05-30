import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_urls", [
    (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/img[1]", [internal_url.MINI_SITE_IMAGE_LAB_SAMPLES]),
    (internal_url.MINI_SITE_FEATURE_2, "//img", [internal_url.MINI_SITE_IMAGE_LAB_PETRI_DISH, internal_url.MINI_SITE_IMAGE_LAB_MICROSCOPE]),
])
def test_get_url_from_images(url: str, xpath: str, expected_urls: list[str], browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.from_images(xpath) == expected_urls
