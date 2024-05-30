import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper.directory import update_path_format_if_windows


@pytest.mark.parametrize("url, xpath, attribute, expected_attribute", [
    (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[2]/div[1]/a", "href", internal_url.MINI_SITE_FEATURE_1),
    (internal_url.MINI_SITE_HOMEPAGE, "/html/head/meta[2]", "name", "viewport"),
    (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/img[1]", "src", update_path_format_if_windows(f"{internal_url.MINI_SITE_DIR}/assets/pexels-chokniti-khongchum-1197604-2280571_medium.jpg")),
    (internal_url.MINI_SITE_FEATURE_1, "/html/head/link[1]", "rel", "stylesheet"),
    (internal_url.MINI_SITE_FEATURE_1, "/html/body/section[1]/div", "class", "hero__text-box"),
])
def test_get_attribute_value(url: str, xpath: str, attribute: str, expected_attribute: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.attribute.value(xpath, attribute) == expected_attribute
