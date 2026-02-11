from pathlib import Path

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.file_png.test_set_1 import FILE_PNG_TEST_SET_DEFAULT

from browserist import Browser


@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_file_png_exception_handling_for_screenshot_visible_portion_method(browser_default_headless: Browser, tmpdir: Path) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    for test in FILE_PNG_TEST_SET_DEFAULT.tests:
        browser.open.url(test.url)
        with test.expectation:
            _ = browser.screenshot.visible_portion(file_name=test.file_name, destination_dir=str(tmpdir)) is not None
