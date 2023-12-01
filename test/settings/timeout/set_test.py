from typing import Any

import pytest
from _config import timeout_settings
from _config.timeout_strategy import BrowserCallable
from _helper import script
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
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
    (browser, browser.click.button_if_contains_text,
     ["/html/body/div/p[2]/a", does_not_exist.TEXT, timeout.VERY_SHORT]),
    (browser, browser.input.select, ["/html/body/div/p[2]/a", timeout.VERY_SHORT]),
    (browser, browser.wait.for_element, [does_not_exist.XPATH, timeout.VERY_SHORT]),
    (browser, browser.wait.until.number_of_window_handles_is, [2, timeout.VERY_SHORT]),
    (browser, browser.wait.until.page_title.contains, [does_not_exist.TEXT, timeout.VERY_SHORT]),
    (browser, browser.wait.until.page_title.changes, ["Example Domain", timeout.VERY_SHORT]),
    (browser, browser.wait.until.page_title.equals, [does_not_exist.TEXT, timeout.VERY_SHORT]),
    (browser, browser.wait.until.text.contains, ["/html/body/div/h1", does_not_exist.TEXT, timeout.VERY_SHORT]),
    (browser, browser.wait.until.text.changes, ["/html/body/div/h1", "Example Domain", timeout.VERY_SHORT]),
    (browser, browser.wait.until.text.equals, ["/html/body/div/h1", does_not_exist.TEXT, timeout.VERY_SHORT]),
    (browser, browser.wait.until.url.contains, [does_not_exist.URL, timeout.VERY_SHORT]),
    (browser, browser.wait.until.url.changes, [internal_url.EXAMPLE_COM, timeout.VERY_SHORT]),
    (browser, browser.wait.until.url.equals, [does_not_exist.URL, timeout.VERY_SHORT]),
])
def test_set_timeout(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    browser = reset_to_not_timed_out(browser)
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser._browser_driver.settings.timeout._is_timed_out is False
    _ = browser_function(*args)
    assert browser._browser_driver.settings.timeout._is_timed_out is True


@pytest.mark.parametrize("browser, browser_function, args", [
    (browser, browser.scroll.page.to_end, []),
])
def test_set_timeout_for_page_without_body(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    browser = reset_to_not_timed_out(browser)
    browser.open.url(internal_url.NO_BODY)
    browser.tool.execute_script(script.REMOVE_BODY_ELEMENT)
    assert browser._browser_driver.settings.timeout._is_timed_out is False
    _ = browser_function(*args)
    assert browser._browser_driver.settings.timeout._is_timed_out is True

# TODO: Add more tests for None return type methods.
