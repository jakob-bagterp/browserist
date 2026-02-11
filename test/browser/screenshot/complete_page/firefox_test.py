from pathlib import Path

import pytest
from _helper import directory, screenshot
from _helper.timeout import reset_to_not_timed_out
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url

from browserist import Browser

MINIMUM_FILE_SIZE = 100_000


@pytest.mark.xdist_group(name="serial_firefox_screenshot_tests")
def test_firefox_get_screenshot_of_complete_page_1(browser_firefox_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page() with default file name and destination."""

    browser = reset_to_not_timed_out(browser_firefox_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    browser.screenshot.complete_page()
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_firefox_screenshot_tests")
def test_firefox_get_screenshot_of_complete_page_2(browser_firefox_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page("image.png") with custom file name and default destination."""

    browser = reset_to_not_timed_out(browser_firefox_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_firefox_screenshot_tests")
def test_firefox_get_screenshot_of_complete_page_3(browser_firefox_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page("image.png", "/screenshots/folder") with custom file name and destination."""

    browser = reset_to_not_timed_out(browser_firefox_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.complete_page(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_firefox_screenshot_tests")
def test_firefox_get_screenshot_of_complete_page_4(browser_firefox_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.complete_page(destination_dir="/screenshots/folder") with default file name and custom destination."""

    browser = reset_to_not_timed_out(browser_firefox_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.complete_page(destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, MINIMUM_FILE_SIZE)
