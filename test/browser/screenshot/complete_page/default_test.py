import pytest
from _helper import screenshot
from _helper.timeout import reset_to_not_timed_out
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser

MINIMUM_FILE_SIZE_EXAMPLE_COM = 12_500  # Single page screenshot.

MINIMUM_FILE_SIZE_W3SCHOOLS_COM = 700_000  # Merge of multiple, e.g. 15-18, files.


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.EXAMPLE_COM, MINIMUM_FILE_SIZE_EXAMPLE_COM),
    (internal_url.W3SCHOOLS_COM, MINIMUM_FILE_SIZE_W3SCHOOLS_COM),
])
def test_default_get_screenshot_of_complete_page_1(url: str, minimum_file_size: int, browser_default_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.complete_page() with default file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(url)
    browser.screenshot.complete_page()
    assert screenshot.images_have_minimum_file_size(tmpdir, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.EXAMPLE_COM, MINIMUM_FILE_SIZE_EXAMPLE_COM),
    (internal_url.W3SCHOOLS_COM, MINIMUM_FILE_SIZE_W3SCHOOLS_COM),
])
def test_default_get_screenshot_of_complete_page_2(url: str, minimum_file_size: int, browser_default_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.complete_page("image.png") with custom file name and default destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(url)
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.EXAMPLE_COM, MINIMUM_FILE_SIZE_EXAMPLE_COM),
    (internal_url.W3SCHOOLS_COM, MINIMUM_FILE_SIZE_W3SCHOOLS_COM),
])
def test_default_get_screenshot_of_complete_page_3(url: str, minimum_file_size: int, browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.complete_page("image.png", "./screenshots") with custom file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.EXAMPLE_COM, MINIMUM_FILE_SIZE_EXAMPLE_COM),
    (internal_url.W3SCHOOLS_COM, MINIMUM_FILE_SIZE_W3SCHOOLS_COM),
])
def test_default_get_screenshot_of_complete_page_4(url: str, minimum_file_size: int, browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.complete_page(destination_dir = "./screenshots") with default file name and custom destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.complete_page(destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, minimum_file_size)
