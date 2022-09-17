from typing import Any

from ...model.browser.base.driver import BrowserDriver


def execute_script(browser_driver: BrowserDriver, script: str, element: object | None = None) -> Any:
    driver = browser_driver.get_webdriver()
    return driver.execute_script(script) if element is None else driver.execute_script(script, element)  # type: ignore
