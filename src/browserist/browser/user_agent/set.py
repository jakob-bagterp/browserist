from ...model.browser.base.driver import BrowserDriver


def set_user_agent(browser_driver: BrowserDriver, user_agent: str) -> None:
    browser_driver.set_user_agent(user_agent)
