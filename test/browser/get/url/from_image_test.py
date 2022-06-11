import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper.directory import update_path_format_if_windows


@pytest.mark.parametrize("url, xpath, expected_url", [
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/img",
     update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png")),
    (internal_url.W3SCHOOLS_COM, "//*[@id='Frontend']/img",
     update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/codeeditor.gif")),
    (internal_url.W3SCHOOLS_COM, "//*[@id='Backend']/img",
     update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/best2.gif")),
])
def test_get_url_from_image(url: str, xpath: str, expected_url: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(url)
    assert browser.get.url.from_image(xpath) == expected_url
