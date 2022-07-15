import pytest
from _mock_data.screenshot import CUSTOM_SCREENSHOT_DIRECTORY
from _mock_data.xpath.method_2 import exception_handling_for_screenshot_methods
from py.path import local

from browserist import Browser
from browserist.browser.screenshot.element import get_screenshot_of_element
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    get_screenshot_of_element,
])
def test_xpath_exception_handling_for_screenshot_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
    tmpdir: local,
) -> None:
    temp_dir = str(tmpdir.mkdir(CUSTOM_SCREENSHOT_DIRECTORY))
    exception_handling_for_screenshot_methods(browser_default_headless, method, temp_dir)
