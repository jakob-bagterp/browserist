from ...model.browser.base.driver import BrowserDriver
from ..tool.execute_script import tool_execute_script


def get_user_agent(browser_driver: BrowserDriver) -> str:
    return str(tool_execute_script(browser_driver, "return navigator.userAgent;"))
