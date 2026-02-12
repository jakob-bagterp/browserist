from pathlib import Path

import pytest
from _helper import directory
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY, CUSTOM_SCREENSHOT_FILENAME
from _mock_data.xpath.method_3 import exception_handling_for_screenshot_methods

from browserist import Browser
from browserist.browser.screenshot.element import get_screenshot_of_element
from browserist.model.type.callable import BrowserMethodWith4ArgumentsCallable


@pytest.mark.parametrize("method", [get_screenshot_of_element])
@pytest.mark.xdist_group(name="serial_screenshot_tests")
def test_xpath_exception_handling_for_screenshot_methods(
    browser_default_headless: Browser, method: BrowserMethodWith4ArgumentsCallable, tmpdir: Path
) -> None:
    temp_dir = directory.create_and_get_temporary(tmpdir, CUSTOM_SCREENSHOT_DIRECTORY)
    exception_handling_for_screenshot_methods(browser_default_headless, method, CUSTOM_SCREENSHOT_FILENAME, temp_dir)
