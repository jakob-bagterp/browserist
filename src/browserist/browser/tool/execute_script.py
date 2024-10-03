from typing import Any

from selenium.webdriver.remote.webelement import WebElement

from ...model.browser.base.driver import BrowserDriver


def tool_execute_script(browser_driver: BrowserDriver, script: str, element: WebElement | None = None) -> Any:
    driver = browser_driver.get_webdriver()
    return driver.execute_script(script) if element is None else driver.execute_script(script, element)  # type: ignore
