from typing import Any

import pytest
from _config import timeout_settings
from _config.timeout_strategy import BrowserCallable
from _helper.timeout import reset_to_not_timed_out, set_to_timed_out
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings

browser_settings = BrowserSettings(
    headless=True,
    disable_images=True,
    timeout=timeout_settings.DEFAULT_STOP
)

browser = Browser(browser_settings)


@pytest.mark.parametrize("browser, browser_function, args", [
    (browser, browser.get.url.current, ()),
])
def test_timeout_strategy_stop(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values are skipped when the timeout is set to stop."""

    browser = set_to_timed_out(browser)
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser_function(*args) is None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None
