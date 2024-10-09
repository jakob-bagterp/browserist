from _constant.user_agent import DEFAULT_USER_AGENT_SNIPPETS
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_user_agent_get(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    user_agent = browser.user_agent.get()
    assert user_agent is not None
    assert any(expected_user_agent_snippet in user_agent for expected_user_agent_snippet in DEFAULT_USER_AGENT_SNIPPETS)
