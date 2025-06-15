from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import tool_execute_script


def get_total_scroll_height(browser_driver: BrowserDriver) -> int:
    script_get_total_scroll_height = """
        return Math.max(
            document.body.scrollHeight, document.documentElement.scrollHeight,
            document.body.offsetHeight, document.documentElement.offsetHeight,
            document.body.clientHeight, document.documentElement.clientHeight
        );"""
    return int(tool_execute_script(browser_driver, script_get_total_scroll_height))
