from pathlib import Path

import pytest
from _helper import directory, screenshot
from _helper.timeout import reset_to_not_timed_out
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url

from browserist import Browser

MINIMUM_FILE_SIZE_MINI_SITE_HOMEPAGE = 7_000  # Single page screenshot.

MINIMUM_FILE_SIZE_SCROLL_LONG_VERTICAL = 400_000  # Merge of multiple, e.g. 10-15, files.


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.MINI_SITE_HOMEPAGE, MINIMUM_FILE_SIZE_MINI_SITE_HOMEPAGE),
    (internal_url.SCROLL_LONG_VERTICAL, MINIMUM_FILE_SIZE_SCROLL_LONG_VERTICAL),
])
@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_default_get_screenshot_of_complete_page_1(url: str, minimum_file_size: int, browser_default_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page() with default file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(url)
    browser.screenshot.complete_page()
    assert screenshot.images_have_minimum_file_size(tmpdir, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.MINI_SITE_HOMEPAGE, MINIMUM_FILE_SIZE_MINI_SITE_HOMEPAGE),
    (internal_url.SCROLL_LONG_VERTICAL, MINIMUM_FILE_SIZE_SCROLL_LONG_VERTICAL),
])
@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_default_get_screenshot_of_complete_page_2(url: str, minimum_file_size: int, browser_default_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page("image.png") with custom file name and default destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(url)
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.MINI_SITE_HOMEPAGE, MINIMUM_FILE_SIZE_MINI_SITE_HOMEPAGE),
    (internal_url.SCROLL_LONG_VERTICAL, MINIMUM_FILE_SIZE_SCROLL_LONG_VERTICAL),
])
@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_default_get_screenshot_of_complete_page_3(url: str, minimum_file_size: int, browser_default_headless: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page("image.png", "/screenshots/folder") with custom file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, minimum_file_size)


@pytest.mark.parametrize("url, minimum_file_size", [
    (internal_url.MINI_SITE_HOMEPAGE, MINIMUM_FILE_SIZE_MINI_SITE_HOMEPAGE),
    (internal_url.SCROLL_LONG_VERTICAL, MINIMUM_FILE_SIZE_SCROLL_LONG_VERTICAL),
])
@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_default_get_screenshot_of_complete_page_4(url: str, minimum_file_size: int, browser_default_headless: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page(destination_dir="/screenshots/folder") with default file name and custom destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.complete_page(destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, minimum_file_size)
