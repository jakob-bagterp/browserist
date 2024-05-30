import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, attribute, expected_attributes", [
    (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[2]/div/a", "href", [internal_url.MINI_SITE_FEATURE_1, internal_url.MINI_SITE_FEATURE_2, internal_url.MINI_SITE_FEATURE_3]),
    (internal_url.MINI_SITE_HOMEPAGE, "/html/head/meta[2]", "name", ["viewport"]),
    (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/img[1]", "alt", ["Lab samples"]),
])
def test_get_attribute_values(url: str, xpath: str, attribute: str, expected_attributes: list[str], browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.attribute.values(xpath, attribute) == expected_attributes
