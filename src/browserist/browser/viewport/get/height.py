from ....model.browser.base.driver import BrowserDriver
from ...tool.execute_script import execute_script


def get_viewport_height(browser_driver: BrowserDriver) -> int:
    return int(execute_script(browser_driver, "return window.innerHeight;"))
