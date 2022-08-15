from typing import Any

from ...model.browser.base.driver import BrowserDriver


def execute_script(browser_driver: BrowserDriver, script: str, element: object | None = None) -> Any:
    driver = browser_driver.get_webdriver()
    if element is None:
        return driver.execute_script(script)  # type: ignore
    else:
        return driver.execute_script(script, element)  # type: ignore
