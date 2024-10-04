import pytest
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings


@pytest.mark.parametrize("user_agent", [
    ("test"),
])
def test_user_agent_set_on_initiation(user_agent: str) -> None:
    settings = BrowserSettings(headless=True, user_agent=user_agent)
    with Browser(settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        user_agent_checked = browser.user_agent.get()
        assert user_agent_checked == user_agent
