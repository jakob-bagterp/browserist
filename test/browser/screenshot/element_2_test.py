from _helper import directory, screenshot
from _helper.timeout import reset_to_not_timed_out
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME, EXAMPLE_COM_VALID_XPATH
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser

MINIMUM_FILE_SIZE = 1_000


def test_get_screenshot_of_element_1_with_default_file_name_and_default_destination(browser_default_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.element("//xpath/to/element") with default file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.screenshot.element(EXAMPLE_COM_VALID_XPATH)
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


def test_get_screenshot_of_element_2_with_custom_file_name_and_default_destination(browser_default_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.element("//xpath/to/element", "image.png") with custom file name and default destination."""

    browser = reset_to_not_timed_out(browser_default_headless_screenshot)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.screenshot.element(EXAMPLE_COM_VALID_XPATH, CUSTOM_SCREENSHOT_FILENAME)
    assert screenshot.images_have_minimum_file_size(tmpdir, MINIMUM_FILE_SIZE)


def test_get_screenshot_of_element_3_with_custom_file_name_and_custom_destination(browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.element("//xpath/to/element", "image.png", "./screenshots") with custom file name and destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.element(EXAMPLE_COM_VALID_XPATH, CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert screenshot.image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME, MINIMUM_FILE_SIZE)


def test_get_screenshot_of_element_4_with_default_file_name_and_custom_destination(browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.element("//xpath/to/element", destination_dir="./screenshots") with default file name and custom destination."""

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    browser.screenshot.element(EXAMPLE_COM_VALID_XPATH, destination_dir=temp_dir)
    assert screenshot.images_have_minimum_file_size(temp_dir, MINIMUM_FILE_SIZE)
