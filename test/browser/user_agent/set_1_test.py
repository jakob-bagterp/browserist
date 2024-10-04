import pytest
from _constant.user_agent import DEFAULT_USER_AGENT_SNIPPETS
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings

# Test initiation of Browser with BrowserSettings
# Test custom user agent on the fly
# TEST VArious browsers + evetual not support errors


@pytest.mark.parametrize("user_agent", [
    ("test"),
])
def test_user_agent_set_on_initiation(user_agent: str) -> None:
    settings = BrowserSettings(headless=True, user_agent=user_agent)
    with Browser(settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        user_agent_checked = browser.user_agent.get()
        assert user_agent_checked == user_agent


@pytest.mark.parametrize("user_agent", [
    ("test"),
])
def test_user_agent_set_on_the_fly(user_agent: str, browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)  # Use and discard the browser, so it doesn't pollute other tests.
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    user_agent_default = browser.user_agent.get()
    assert any(expected_user_agent_snippet in user_agent_default for expected_user_agent_snippet in DEFAULT_USER_AGENT_SNIPPETS)
    browser.user_agent.set(user_agent)
    user_agent_custom = browser.user_agent.get()
    assert user_agent_custom == user_agent
