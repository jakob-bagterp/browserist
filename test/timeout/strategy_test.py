from typing import Any

import pytest
from _config.timeout_strategy import BrowserCallable
from _helper.timeout import reset_to_not_timed_out, set_to_timed_out
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

browser_settings = BrowserSettings(
    headless=True,
    disable_images=True,
    timeout=TimeoutSettings(seconds=1)
)

browser = Browser(browser_settings)

METHODS_WITH_RETURN_VALUES = [
    (browser, browser.check_if.contains_any_text, ["//*[@id='main']/div[1]/div/h1"]),
    (browser, browser.check_if.contains_text, ["//*[@id='main']/div[1]/div/h1", "Learn to Code"]),
    (browser, browser.check_if.does_exist, ["//*[@id='main']/div[1]/div/h1"]),
    (browser, browser.check_if.is_clickable, ["//*[@id='main']/div[1]/div/h4/a"]),
    (browser, browser.check_if.is_disabled, ["//*[@id='main']/div[1]/div/h1"]),
    (browser, browser.check_if.is_displayed, ["//*[@id='main']/div[1]/div/h1"]),
    (browser, browser.check_if.is_enabled, ["//*[@id='main']/div[1]/div/h1"]),
    (browser, browser.check_if.is_image_loaded, ["//*[@id='Frontend']/img"]),
    (browser, browser.get.url.current, []),
]


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
def test_timeout_strategy_stop(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values are skipped when the timeout is set to stop."""

    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.STOP
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser = set_to_timed_out(browser)
    assert browser_function(*args) is None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
def test_timeout_strategy_continue(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values aren't skipped when the timeout is set to continue."""

    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.CONTINUE
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser = set_to_timed_out(browser)
    assert browser_function(*args) is not None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None
