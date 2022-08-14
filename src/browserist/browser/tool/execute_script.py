from ...model.browser.base.driver import BrowserDriver


def execute_script(browser_driver: BrowserDriver, script: str) -> None:
    driver = browser_driver.get_webdriver()
    driver.execute_script(script)  # type: ignore
