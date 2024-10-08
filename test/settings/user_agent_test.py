from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import external_url, internal_url

from browserist import Browser, BrowserSettings, BrowserType

USER_AGENT_TEST = "test"


def test_user_agent_set_on_initiation_with_default_browser() -> None:
    browser_settings = BrowserSettings(headless=True, user_agent=USER_AGENT_TEST)
    with Browser(browser_settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)

        # Troubleshooting test:
        # headline = browser.get.text("//h1")
        # assert headline == "Welcome"
        browser.open.url(external_url.EXAMPLE_COM)
        headline = browser.get.text("//h1")
        assert headline == "Example Domain"

        user_agent_checked = browser.user_agent.get()
        assert user_agent_checked == USER_AGENT_TEST


@pytest.mark.parametrize("browser_settings, expectation", [
    (BrowserSettings(type=BrowserType.CHROME, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
    (BrowserSettings(type=BrowserType.EDGE, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
    (BrowserSettings(type=BrowserType.FIREFOX, headless=True, user_agent=USER_AGENT_TEST), does_not_raise()),
])
def test_user_agent_set_on_initiation_with_various_browsers(browser_settings: BrowserSettings, expectation: Any) -> None:
    with expectation:
        with Browser(browser_settings) as browser:
            browser.open.url(internal_url.MINI_SITE_HOMEPAGE)

            # Troubleshooting test:
            # headline = browser.get.text("//h1")
            # assert headline == "Welcome"
            browser.open.url(external_url.EXAMPLE_COM)
            headline = browser.get.text("//h1")
            assert headline == "Example Domain"

            user_agent_checked = browser.user_agent.get()
            assert user_agent_checked == browser_settings.user_agent
