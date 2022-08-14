from typing import Any

import pytest
from _config.timeout_strategy import BrowserCallable
from _helper.timeout import reset_to_not_timed_out, set_to_timed_out
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, TimeoutStrategy

browser_settings = BrowserSettings(
    headless=True,
    disable_images=True,
)

browser = Browser(browser_settings)

METHODS_WITH_RETURN_VALUES = [
    (browser, browser.check_if.contains_any_text, ["/html/body/div/h1"]),
    (browser, browser.check_if.contains_text, ["/html/body/div/h1", "Example Domain"]),
    (browser, browser.check_if.does_exist, ["/html/body/div/h1"]),
    (browser, browser.check_if.is_clickable, ["/html/body/div/p[2]/a"]),
    (browser, browser.check_if.is_disabled, ["/html/body/div/h1"]),
    (browser, browser.check_if.is_displayed, ["/html/body/div/h1"]),
    (browser, browser.check_if.is_enabled, ["/html/body/div/h1"]),
    (browser, browser.check_if.is_image_loaded, ["/html/body/div/h1"]),
    (browser, browser.get.url.current, []),
]


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
def test_timeout_strategy_stop(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values are skipped when the timeout is set to stop."""

    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.STOP
    browser = set_to_timed_out(browser)
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser_function(*args) is None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
def test_timeout_strategy_continue(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values aren't skipped when the timeout is set to continue."""

    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.CONTINUE
    browser = set_to_timed_out(browser)
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser_function(*args) is not None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None
