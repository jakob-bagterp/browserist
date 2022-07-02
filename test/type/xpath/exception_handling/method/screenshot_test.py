import pytest
from _config.browser_settings.default import DEFAULT as DEFAULT_BROWSER_SETTINGS
from _mock_data.xpath.method_2 import exception_handling_for_methods_with_3_arguments_or_more

from browserist import Browser
from browserist.browser.screenshot.element import get_screenshot_of_element
from browserist.model.type.callable import BrowserMethodWith3ArgumentsCallable


@pytest.mark.parametrize("method", [
    get_screenshot_of_element,
])
def test_xpath_exception_handling_for_screenshot_methods(
    browser_default_headless: Browser,
    method: BrowserMethodWith3ArgumentsCallable,
) -> None:
    exception_handling_for_methods_with_3_arguments_or_more(browser_default_headless, method, DEFAULT_BROWSER_SETTINGS)
