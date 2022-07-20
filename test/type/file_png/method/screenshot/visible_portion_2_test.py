from _mock_data.file_png.test_set_1 import FILE_PNG_TEST_SET_DEFAULT
from py.path import local

from browserist import Browser


def test_file_png_exception_handling_for_screenshot_visible_portion_method(browser_default_headless: Browser, tmpdir: local) -> None:
    browser = browser_default_headless
    for test in FILE_PNG_TEST_SET_DEFAULT.tests:
        browser.open.url(test.url)
        with test.expectation:
            _ = browser.screenshot.visible_portion(file_name=test.file_name, destination_dir=str(tmpdir)) is not None
