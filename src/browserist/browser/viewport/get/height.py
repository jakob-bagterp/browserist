from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import tool_execute_script


def get_viewport_height(browser_driver: BrowserDriver) -> int:
    return int(tool_execute_script(browser_driver, "return window.innerHeight;"))
