from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import tool_execute_script


def get_total_scroll_width(browser_driver: BrowserDriver) -> int:
    script_get_total_scroll_width = """return Math.max(
        document.body.scrollWidth, document.documentElement.scrollWidth,
        document.body.offsetWidth, document.documentElement.offsetWidth,
        document.body.clientWidth, document.documentElement.clientWidth
    );"""
    return int(tool_execute_script(browser_driver, script_get_total_scroll_width))
