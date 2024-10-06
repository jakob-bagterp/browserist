from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, BrowserType


@pytest.mark.parametrize("browser_type, user_agent, expectation", [
    (BrowserType.CHROME, "test", does_not_raise()),
    (BrowserType.EDGE, "test", does_not_raise()),
    (BrowserType.FIREFOX, "test", does_not_raise()),
])
def test_user_agent_set_on_initiation(browser_type: BrowserType, user_agent: str, expectation: Any) -> None:
    settings = BrowserSettings(type=browser_type, headless=True, user_agent=user_agent)
    with expectation:
        with Browser(settings) as browser:
            browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
            user_agent_checked = browser.user_agent.get()
            assert user_agent_checked == user_agent
