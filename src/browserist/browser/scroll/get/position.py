from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import tool_execute_script


def get_scroll_position(browser_driver: BrowserDriver) -> tuple[int, int]:
    x = int(tool_execute_script(browser_driver, "return window.pageXOffset;"))
    y = int(tool_execute_script(browser_driver, "return window.pageYOffset;"))
    return x, y
