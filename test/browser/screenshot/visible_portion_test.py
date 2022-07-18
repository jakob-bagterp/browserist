from _helper.screenshot.element_or_visible_portion import image_has_minimum_file_size, images_have_minimum_file_size
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser


def test_get_screenshot_of_visible_portion_1(browser_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion() with default file name and destination."""

    browser = browser_headless_screenshot
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.screenshot.visible_portion()
    assert images_have_minimum_file_size(str(tmpdir))


def test_get_screenshot_of_visible_portion_2(browser_headless_screenshot: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion("image.png") with custom file name and default destination."""

    browser = browser_headless_screenshot
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME)
    assert images_have_minimum_file_size(str(tmpdir))


def test_get_screenshot_of_visible_portion_3(browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion("image.png", "./screenshots") with custom file name and destination."""

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.visible_portion(CUSTOM_SCREENSHOT_FILENAME, temp_dir)
    assert image_has_minimum_file_size(temp_dir, CUSTOM_SCREENSHOT_FILENAME)


def test_get_screenshot_of_visible_portion_4(browser_default_headless: Browser, tmpdir: local) -> None:
    """Test of browser.screenshot.visible_portion(destination_dir = "./screenshots") with default file name and custom destination."""

    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    browser.screenshot.visible_portion(destination_dir=temp_dir)
    assert images_have_minimum_file_size(temp_dir)
