from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _constant.user_agent import DEFAULT_USER_AGENT_SNIPPETS
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, BrowserType
from browserist.exception.user_agent import ChangeUserAgentOnTheFlyNotSupportedException
from browserist.helper import operating_system


@pytest.mark.parametrize(
    "browser_settings, user_agent, expectation",
    [
        (BrowserSettings(type=BrowserType.CHROME, headless=True), "test", does_not_raise()),
        (BrowserSettings(type=BrowserType.EDGE, headless=True), "test", does_not_raise()),
        (
            BrowserSettings(type=BrowserType.FIREFOX, headless=True),
            "test",
            pytest.raises(ChangeUserAgentOnTheFlyNotSupportedException),
        ),
    ],
)
def test_user_agent_set_on_the_fly(browser_settings: BrowserSettings, user_agent: str, expectation: Any) -> None:
    if operating_system.is_macos() and browser_settings.type is BrowserType.EDGE:
        pytest.skip("Microsoft Edge is not supported on macOS.")
        return
    with Browser(browser_settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        user_agent_default = browser.user_agent.get()
        assert any(
            expected_user_agent_snippet in user_agent_default
            for expected_user_agent_snippet in DEFAULT_USER_AGENT_SNIPPETS
        )
        with expectation:
            browser.user_agent.set(user_agent)
            user_agent_custom = browser.user_agent.get()
            assert user_agent_custom == user_agent
