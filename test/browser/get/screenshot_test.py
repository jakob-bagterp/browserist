import os

from _helper import internal_url
from py.path import local

from browserist import Browser

CUSTOM_SCREENSHOT_DIRECTORY = "screenshot"
CUSTOM_SCREENSHOT_FILENAME = "screenshot.png"
MINIMUM_FILE_SIZE = 1000


def image_has_minimum_file_size(directory: str, file_name: str) -> bool:
    return os.path.getsize(f"{directory}/{file_name}") > MINIMUM_FILE_SIZE


def images_have_minimum_file_size(directory: str) -> bool:
    def absolute_path(file: str) -> str:
        return os.path.join(directory, file)

    files = [absolute_path(file) for file in os.listdir(directory) if os.path.isfile(absolute_path(file))]
    return all(os.path.getsize(file) > MINIMUM_FILE_SIZE for file in files)


def test_get_screenshot_1(browser_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.get.screenshot() with default file name and destination."""

    browser = browser_headless_screenshot
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.get.screenshot()
    assert images_have_minimum_file_size(str(tmpdir))


def test_get_screenshot_2(browser_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.get.screenshot("image.png") with custom file name and default destination."""

    browser = browser_headless_screenshot
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.get.screenshot(CUSTOM_SCREENSHOT_FILENAME)
    assert images_have_minimum_file_size(str(tmpdir))


def test_get_screenshot_3(browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.get.screenshot("image.png", "./screenshots") with custom file name and destination."""

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.get.screenshot(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME)
