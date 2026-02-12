from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, BrowserType
from browserist.helper import operating_system

USER_AGENT_TEST = "test"


def test_user_agent_set_on_initiation_with_default_browser() -> None:
    browser_settings = BrowserSettings(headless=True, user_agent=USER_AGENT_TEST)
    with Browser(browser_settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        user_agent_checked = browser.user_agent.get()
        assert user_agent_checked == USER_AGENT_TEST


@pytest.mark.parametrize(
    "browser_settings, expectation",
    [
        (BrowserSettings(type=BrowserType.CHROME, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
        (BrowserSettings(type=BrowserType.EDGE, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
        (BrowserSettings(type=BrowserType.FIREFOX, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
    ],
)
def test_user_agent_set_on_initiation_with_various_browsers(
    browser_settings: BrowserSettings, expectation: Any
) -> None:
    if operating_system.is_macos() and browser_settings.type is BrowserType.EDGE:
        pytest.skip("Microsoft Edge is not supported on macOS.")
        return
    with expectation:
        with Browser(browser_settings) as browser:
            browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
            user_agent_checked = browser.user_agent.get()
            assert user_agent_checked == USER_AGENT_TEST
