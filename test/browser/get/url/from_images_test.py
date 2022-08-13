import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper.directory import update_path_format_if_windows


@pytest.mark.parametrize("url, xpath, expected_urls", [
    (internal_url.W3SCHOOLS_COM, "//*[@id='bgcodeimg2']/div/img",
     [f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png"]),
    (internal_url.W3SCHOOLS_COM, "//img", [
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/codeeditor.gif"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/best2.gif"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/how-spaces-works3.png"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/colorpicker.png"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/w3lynx_200.png"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/w3css_templates.jpg"),
        update_path_format_if_windows(f"{internal_url.W3SCHOOLS_COM_DIR}/w3schools_logo_500_04AA6D.png"),
    ]),
])
def test_get_url_from_images(url: str, xpath: str, expected_urls: list[str], browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.url.from_images(xpath) == expected_urls
