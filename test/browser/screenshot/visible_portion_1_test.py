from pathlib import Path

import pytest
from _helper import directory, screenshot
from _helper.timeout import reset_to_not_timed_out
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url

from browserist import Browser

MINIMUM_FILE_SIZE = 1_000


@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_get_screenshot_of_visible_portion_1(browser_default_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.visible_portion() with default file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.screenshot.visible_portion()
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_get_screenshot_of_visible_portion_2(browser_default_headless_screenshot: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.visible_portion("image.png") with custom file name and default destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_get_screenshot_of_visible_portion_3(browser_default_headless: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.visible_portion("image.png", "/screenshots/folder") with custom file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, MINIMUM_FILE_SIZE)


@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_get_screenshot_of_visible_portion_4(browser_default_headless: Browser, tmpdir: Path) -> None:
    """Test of browser.screenshot.visible_portion(destination_dir="/screenshots/folder") with default file name and custom destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.visible_portion(destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, MINIMUM_FILE_SIZE)
