from typing import Any

import pytest
from _config import timeout_settings
from _config.timeout_strategy import BrowserCallable
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings
from browserist.constant import timeout

browser_settings = BrowserSettings(
    headless=True,
    disable_images=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

browser = Browser(browser_settings)


@pytest.mark.parametrize("browser, browser_function, args", [
    (browser, browser.wait.for_element, ("/does/not/exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.number_of_window_handles_is, (2, timeout.VERY_SHORT)),
    (browser, browser.wait.until.page_title.contains, ("does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.page_title.changes, ("does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.page_title.equals, ("does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.text.contains, ("/does/not/exist", "does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.text.changes, ("/does/not/exist", "does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.text.equals, ("/does/not/exist", "does not exist", timeout.VERY_SHORT)),
    (browser, browser.wait.until.url.contains, ("https://www.does-not-exist.com", timeout.VERY_SHORT)),
    (browser, browser.wait.until.url.changes, ("https://www.does-not-exist.com", timeout.VERY_SHORT)),
    (browser, browser.wait.until.url.equals, ("https://www.does-not-exist.com", timeout.VERY_SHORT)),
])
def test_set_timeout(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    browser.open.url(internal_url.EXAMPLE_COM)
    browser = reset_to_not_timed_out(browser)
    assert browser._browser_driver.settings.timeout._is_timed_out is False
    _ = browser_function(*args)
    assert browser._browser_driver.settings.timeout._is_timed_out is True
