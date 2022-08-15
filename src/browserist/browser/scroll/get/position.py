from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import execute_script


def get_scroll_position(browser_driver: BrowserDriver) -> tuple[int, int]:
    x = int(execute_script(browser_driver, "return window.pageXOffset;"))
    y = int(execute_script(browser_driver, "return window.pageYOffset;"))
    return x, y
